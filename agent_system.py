import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langgraph.graph import START, StateGraph, MessagesState
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_core.messages import SystemMessage

# Load environment variables
load_dotenv()

# Fetch Azure credentials
azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_version = os.getenv("API_version")
deployment_name = os.getenv("DEPLOYMENT_NAME")

# Tools with docstrings
def add(a: int, b: int) -> int:
    """Adds two integers and returns the result."""
    return a + b

def multiply(a: int, b: int) -> int:
    """Multiplies two integers and returns the result."""
    return a * b

def divide(a: int, b: int) -> float:
    """Divides a by b and returns the result as a float."""
    return a / b

tools = [add, multiply, divide]

# Configure Azure OpenAI
llm = AzureChatOpenAI(
    azure_endpoint=azure_endpoint,
    api_key=azure_api_key,
    deployment_name=deployment_name,
    api_version=api_version
)

llm_with_tools = llm.bind_tools(tools)

# System message
sys_msg = SystemMessage(content="You are a helpful assistant tasked with performing arithmetic operations.")

# Node
def assistant(state: MessagesState):
    return {"messages": [llm_with_tools.invoke([sys_msg] + state["messages"])]}

# Build graph
builder = StateGraph(MessagesState)
builder.add_node("assistant", assistant)
builder.add_node("tools", ToolNode(tools))
builder.add_edge(START, "assistant")
builder.add_conditional_edges("assistant", tools_condition)
builder.add_edge("tools", "assistant")

# Compile graph
graph = builder.compile()