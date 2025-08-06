from google.adk.agents import Agent
from google.adk.tools.retrieval.vertex_ai_rag_retrieval import VertexAiRagRetrieval
from google.adk.tools.agent_tool import AgentTool
from . import prompt
import os
from vertexai.preview import rag


MODEL = "gemini-2.5-pro"

ask_vertex_retrieval = VertexAiRagRetrieval(
    name="retrieve_rag_documentation",
    description="Retrieve building code documentation for specific design elements.",
    rag_resources=[rag.RagResource(rag_corpus=os.environ.get("RAG_CORPUS"))],
    similarity_top_k=10,
    vector_distance_threshold=0.6,
)


rag_agent = Agent(
    model=MODEL,
    name="rag_agent",
    instruction=prompt.RAG_AGENT_PROMPT,
    tools=[ask_vertex_retrieval],
    output_key="building_code_validated",
)
