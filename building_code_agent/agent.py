from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from . import prompt
import os
from vertexai.preview import rag
from .subagents.rag_agent import rag_agent

# from .sub_agents.blueprint_reading_agent import blueprint_reading_agent

MODEL = "gemini-2.5-pro"


building_code_validation_agent = Agent(
    name="building_code_validation_agent",
    model=MODEL,
    description="Validates blueprints against building code by generating queries and checking with the RAG tool.",
    instruction=prompt.BUILDING_CODE_AGENT_PROMPT,
    output_key="building_code_validated",
    tools=[AgentTool(agent=rag_agent)],
)

root_agent = building_code_validation_agent
