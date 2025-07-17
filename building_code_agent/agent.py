from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from . import prompt
# from .sub_agents.blueprint_reading_agent import blueprint_reading_agent

MODEL = "gemini-2.5-pro"


building_code_validation_agent = LlmAgent(
    name="building_code_validation_agent",
    model=MODEL,
    description= "Analyses construction blueprint PDFs provided by users and validates it against building codes to check if the blueprint is up to code.",
    instruction=prompt.BUILDING_CODE_AGENT_PROMPT,
    output_key="building_code_validated",
    # tools=[
    #     AgentTool(agent=blueprint_reading_agent)
    # ]
        
)

root_agent = building_code_validation_agent