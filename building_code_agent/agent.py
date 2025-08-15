from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from . import prompt
import os
from vertexai.preview import reasoning_engines
from .subagents.rag_agent import rag_agent
from vertexai import agent_engines
import vertexai

MODEL = "gemini-2.5-pro"
GOOGLE_CLOUD_PROJECT = os.environ["GOOGLE_CLOUD_PROJECT"]
GOOGLE_CLOUD_LOCATION = os.environ["GOOGLE_CLOUD_LOCATION"]
STORAGE_BUCKET = os.environ["STORAGE_BUCKET"]
# GOOGLE_API_KEY = os.environ["GOOGLE_API_KEY"]
GOOGLE_GENAI_USE_VERTEXAI = os.environ["GOOGLE_GENAI_USE_VERTEXAI"]
STAGING_BUCKET = "gs://" + STORAGE_BUCKET
PROJECT_ID = GOOGLE_CLOUD_PROJECT
# staging_bucket = STAGING_BUCKET
# ROOT_AGENT_NAME = "adk_renovation_agent"

building_code_validation_agent = Agent(
    name="building_code_validation_agent",
    model=MODEL,
    description="Validates blueprints against building code by generating queries and checking with the RAG tool.",
    instruction=prompt.BUILDING_CODE_AGENT_PROMPT,
    output_key="building_code_validated",
    tools=[AgentTool(agent=rag_agent)],
)


vertexai.init(
    project=PROJECT_ID,
    location=GOOGLE_CLOUD_LOCATION,
    staging_bucket=STAGING_BUCKET,
)
root_agent = building_code_validation_agent
