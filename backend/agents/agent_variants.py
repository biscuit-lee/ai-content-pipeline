import os
import json
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool, AgentType
from langchain.utilities import SerpAPIWrapper


class Agent3:
    def __init__(self, model="deepseek/deepseek-chat-v3.1:free"):
        # Ensure API keys are set
        if not os.getenv("OPEN_ROUTER_API_KEY"):
            raise ValueError("OPEN_ROUTER_API_KEY not set in environment")
        if not os.getenv("SERPAPI_API_KEY"):
            raise ValueError("SERPAPI_API_KEY not set in environment")
        
        self.llm = ChatOpenAI(
            api_key=os.getenv("OPEN_ROUTER_API_KEY"),
            base_url="https://openrouter.ai/api/v1",
            model=model,
        )

        # Fake tool for clean JSON output
        def return_json(s: str) -> str:
            # Extract the last JSON object if Thoughts are present
            import re, json
            matches = re.findall(r"\{.*\}", s, re.DOTALL)
            if matches:
                return matches[-1]  # return the last JSON-looking string
            return s


        # Set up the search tool
        self.search_tool = SerpAPIWrapper(serpapi_api_key=os.getenv("SERPAPI_API_KEY"))

        # Create tools list
        self.tools = [
            Tool(
                name="WebSearch",
                func=self.search_tool.run,
                description="Useful for looking up current events or factual information on the web."
            ),
            Tool(
                name="ReturnJSON",
                func=return_json,
                description="Use this at the end to return the final structured JSON output."
            )
        ]

        # Initialize the agent
        self.agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            handle_parsing_errors=True,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True,
            tool_choice="ReturnJSON"
        )
    
    def ask_llm(self, query):
        """Run a query through the agent"""
        return self.deserialize_response(self.agent.run(query))
    

    def deserialize_response(self, response) -> dict:
        try:
            if response.startswith("`") and response.endswith("`"):
                response = response[1:-1]  # remove the backticks

            if '```json' in response:
                # Extract the JSON part from the response
                response = response.split('```json')[1].split('```')[0].strip()
            if not isinstance(response, dict):
                return json.loads(response)
            return response
        except json.JSONDecodeError:
            print(f"Failed to parse JSON: {response}")
            return None



class Agent2:
    def ask_llm(self, prompt):
        
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=os.getenv("OPEN_ROUTER_API_KEY"),
        )

        completion = client.chat.completions.create(
        model="deepseek/deepseek-chat-v3.1:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
         ]
        )

        res = self.deserialize_response(completion.choices[0].message.content)
        return res

    def deserialize_response(self, response) -> dict:

        try:
            if response.startswith("`") and response.endswith("`"):
                response = response[1:-1]  # remove the backticks

            if '```json' in response:
                # Extract the JSON part from the response
                response = response.split('```json')[1].split('```')[0].strip()
            if not isinstance(response, dict):
                return json.loads(response)
            return response
        except json.JSONDecodeError:
            print(f"Failed to parse JSON: {response}")
            return None
        
