from langchain.agents import Tool, initialize_agent, AgentType
from backend.agents.base_agent import Agent
from langchain.utilities import SerpAPIWrapper
import os


class LangChainAgent:
    def __init__(self):
        self.agent_llm = Agent()
        self.search_tool = SerpAPIWrapper(serpapi_api_key=os.getenv("SERPAPI_API_KEY"))

        # Wrap tools for LangChain
        self.tools = [
            Tool(
                name="WebSearch",
                func=self.search_tool.run,
                description="Useful for looking up current events or factual information on the web."
            )
        ]

        # Initialize agent with LangChain
        self.agent = initialize_agent(
            tools=self.tools,
            llm=self,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True
        )

    def run(self, prompt: str):
        """
        LangChain expects a callable with prompt -> str
        """
        return self.agent.run(prompt)



