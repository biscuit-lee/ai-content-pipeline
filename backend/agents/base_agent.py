import os
import json
import re
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langchain.agents import Tool, initialize_agent, AgentType


class Agent:
    def __init__(self, model="openai/gpt-oss-20b:free"):
        # Ensure API keys are set
        if not os.getenv("OPEN_ROUTER_API_KEY"):
            raise ValueError("OPEN_ROUTER_API_KEY not set in environment")
        if not os.getenv("SERPAPI_API_KEY"):
            raise ValueError("SERPAPI_API_KEY not set in environment")
        
        self.llm = ChatOpenAI(
            api_key=os.getenv("OPEN_ROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
            model=model,
            temperature=0.7,
            max_tokens=12000
        )

        self.search_tool = TavilySearch(api_key=os.getenv("TAVILY_API_KEY"))

        # Fixed JSON return tool
        def return_json(json_input: str) -> str:
            """Extract and return clean JSON from agent output"""
            try:
                parsed = json.loads(json_input)
                print("RETURNED PARSED ", json_input)
                return parsed
            except json.JSONDecodeError:
                print("ERROR ERROR JSON ", json_input)
                return self._extract_clean_json(json_input)

        # Create tools list
        self.tools = [
            Tool(
                name="WebSearch",
                func=self.search_tool.run,
                description="Search the web for current information, trends, or examples. Use this to find recent business examples or verify facts."
            ),
            Tool(
                name="ReturnJSON", 
                func=return_json,
                description="FINAL STEP: Return the complete JSON object for the YouTube topic. Use this only when you have all the information needed."
            )
        ]

        # Initialize agent with custom prompt
        self.agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=4,
            early_stopping_method="generate",
            return_intermediate_steps=False
        )
    
    def _extract_clean_json(self, text: str) -> str:
        """Extract clean JSON from ReAct formatted text"""
        
        # Look for Action Input: followed by JSON
        action_input_pattern = r'Action Input:\s*(\{.*\})'
        matches = re.findall(action_input_pattern, text, re.DOTALL | re.MULTILINE)
        
        if matches:
            for json_str in reversed(matches):
                try:
                    parsed = json.loads(json_str)
                    return json.dumps(parsed, separators=(',', ':'))
                except json.JSONDecodeError:
                    continue
        
        # Fallback: Remove ReAct formatting lines and find JSON
        lines = text.split('\n')
        cleaned_lines = []
        
        for line in lines:
            stripped = line.strip()
            if (stripped.startswith('Thought:') or 
                stripped.startswith('Action:') or 
                stripped.startswith('Action Input:') or 
                stripped.startswith('Observation:') or
                stripped.startswith('> Finished') or
                stripped.startswith('Final Answer:')):
                continue
            cleaned_lines.append(line)
        
        cleaned_text = '\n'.join(cleaned_lines)
        
        # Find JSON objects using brace matching
        json_objects = []
        brace_count = 0
        start_pos = None
        
        for i, char in enumerate(cleaned_text):
            if char == '{':
                if brace_count == 0:
                    start_pos = i
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0 and start_pos is not None:
                    json_candidate = cleaned_text[start_pos:i+1]
                    json_objects.append(json_candidate)
        
        for json_str in reversed(json_objects):
            try:
                parsed = json.loads(json_str)
                return json.dumps(parsed, separators=(',', ':'))
            except json.JSONDecodeError:
                continue
        
        return '{"error": "No valid JSON found"}'
    
    def ask_llm(self, query=None) -> dict:
        """Run a query through the agent"""
        
        if query is None:
            query = """Generate a viral YouTube topic about business psychology.

                STEPS:
                1. WebSearch: Find recent counterintuitive business examples
                2. ReturnJSON: Return complete topic JSON

                REQUIREMENTS:
                - Focus on why successful companies do counterintuitive things
                - 3+ real company examples
                - 8+ viral potential score
                - Use ReturnJSON tool for final output"""
            
        try:
            result = self.agent.run(query)
            return self.deserialize_response(result)
        except Exception as e:
            print(f"Agent error: {e}")
            return self._fallback_generation(query)
    
    def ask_llm_no_search(self, prompt):
        res = self.llm.invoke([{"role": "user", "content": prompt}]).content
        return self.deserialize_response(res)

    def ask_llm_with_review_loop(self, query, revision_rules=None, max_revisions=3):
        """Generate a draft, have a reviewer evaluate it, then rewrite until requirements are met."""

        draft = self.ask_llm(query)

        if not revision_rules:
            return draft

        for i in range(max_revisions):
            review_prompt = f"""
            You are an expert YouTube script reviewer.

            --- REVISION RULES ---
            {revision_rules}

            --- CURRENT DRAFT ---
            {draft}

            --- TASK ---
            1. Review the draft and indicate if all rules are met.
            2. Output structured JSON:
               {{
                 "requirements_met": true/false,
                 "missing_elements": ["list of issues"],
                 "suggested_fixes": ["short guidance for rewriting"]
               }}
            Only output JSON.
            """
            review = self.ask_llm_no_search(review_prompt)

            if not isinstance(review, dict):
                try:
                    review = json.loads(review)
                except json.JSONDecodeError:
                    review = {"requirements_met": False, "missing_elements": [], "suggested_fixes": []}

            if review.get("requirements_met", False):
                return draft

            rewrite_prompt = f"""
            You are now the script writer.

            --- CURRENT DRAFT ---
            {draft}

            --- REVIEW FEEDBACK ---
            {json.dumps(review)}

            --- TASK ---
            Rewrite the draft to fully address all issues in 'missing_elements' and 'suggested_fixes'.
            Keep the output JSON structure the same as the original draft.
            Do not add anything before or after the json, just pure json returns
            """
            draft = self.ask_llm_no_search(rewrite_prompt)

        return draft

    def _fallback_generation(self, query):
        """Fallback method using direct LLM call if agent fails"""
        fallback_prompt = f"""Generate a viral YouTube topic about business psychology. Return ONLY valid JSON.

Schema:
{{
    "topic_title": "Why [Company] Does [Counterintuitive Thing]",
    "hook_angle": "Attention-grabbing opener...",
    "central_mystery": "The psychological puzzle",
    "key_examples": ["Example 1", "Example 2", "Example 3"],
    "psychological_principles": ["Principle 1", "Principle 2", "Principle 3"],
    "viral_potential_score": 9,
    "why_it_works": "Viral appeal explanation"
}}

Focus on: {query}

JSON only:"""
        
        try:
            response = self.llm.invoke([{"role": "user", "content": fallback_prompt}])
            if hasattr(response, 'content'):
                response = response.content
            return self.deserialize_response(response)
        except Exception as e:
            print(f"Fallback also failed: {e}")
            return None

    def deserialize_response(self, response) -> dict:
        """Enhanced JSON parsing with better error handling"""
        print(f"deserialize_response received: {type(response)} - {response}")
        
        if not response:
            return None
            
        try:
            response = response.strip()
            if isinstance(response, dict):
                print("Response is already a dict, returning as-is")
                return response
                
            if isinstance(response, str):
                if response.strip().startswith("{'") or response.strip().startswith('{"'):
                    try:
                        import ast
                        parsed = ast.literal_eval(response)
                        if isinstance(parsed, dict):
                            return parsed
                    except:
                        pass
                
                if response.startswith("```json"):
                    parts = response.split("```json", 1)
                    content = parts[1] if len(parts) > 1 else parts[0]
                    # Split only if there *is* a closing ```
                    if "```" in content:
                        response = content.split("```", 1)[0].strip()
                    else:
                        response = content.strip()

                elif response.startswith("```"):
                    response = response.split("```")[1].split("```")[0].strip()
                
                response = response.strip("`")
                
                if any(keyword in response for keyword in ['Action Input:', 'Thought:', 'Observation:']):
                    response = self._extract_clean_json(response)
                
                parsed = json.loads(response)
                return parsed
        except json.JSONDecodeError as e:
            print(f"Failed to parse JSON: {e}")
            print(f"Response was: {response}")
            return None
    
    def _validate_schema(self, data: dict) -> bool:
        """Validate that the JSON matches our required schema"""
        required_fields = [
            "topic_title", "hook_angle", "central_mystery",
            "key_examples", "psychological_principles", 
            "viral_potential_score", "why_it_works"
        ]
        
        for field in required_fields:
            if field not in data:
                print(f"Missing required field: {field}")
                return False
        
        if not isinstance(data.get("key_examples"), list):
            print("key_examples must be a list")
            return False
            
        if not isinstance(data.get("psychological_principles"), list):
            print("psychological_principles must be a list")
            return False
            
        if not isinstance(data.get("viral_potential_score"), (int, float)):
            print("viral_potential_score must be a number")
            return False
            
        return True