# if you dont use pipenv uncomment the following:
#from dotenv import load_dotenv
import os

# Load environment variables from .env file
if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv()

# Step 1: Setup API Keys for Groq, OpenAI, and Tavily
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Step 2: Setup LLM & Tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

# Initialize LLMs with error handling
try:
    openai_llm = ChatOpenAI(model="gpt-4o-mini")
except Exception as e:
    print(f"Error initializing OpenAI LLM: {e}")
    openai_llm = None

try:
    groq_llm = ChatGroq(model="llama-3.3-70b-versatile")
except Exception as e:
    print(f"Error initializing Groq LLM: {e}")
    groq_llm = None

# Initialize search tool with error handling
try:
    search_tool = TavilySearchResults(max_results=2)
except Exception as e:
    print(f"Error initializing Tavily search tool: {e}")
    search_tool = None

# Step 3: Setup AI Agent with Search tool functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

# Define system prompt with error handling
try:
    system_prompt = "Act as an AI chatbot who is smart and friendly"
except Exception as e:
    print(f"Error defining system prompt: {e}")
    system_prompt = ""

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    """
    Get response from AI agent with search tool functionality.

    Args:
        llm_id (str): LLM ID.
        query (str): User query.
        allow_search (bool): Allow search or not.
        system_prompt (str): System prompt.
        provider (str): Provider (Groq or OpenAI).

    Returns:
        str: AI response.
    """
    if provider == "Groq":
        llm = ChatGroq(model=llm_id)
    elif provider == "OpenAI":
        llm = ChatOpenAI(model=llm_id)

    tools = [TavilySearchResults(max_results=2)] if allow_search else []
    agent = create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )
    state = {"messages": query}
    response = agent.invoke(state)
    messages = response.get("messages")
    ai_messages = [message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1] if ai_messages else ""
    load_dotenv()

#Step1: Setup API Keys for Groq, OpenAI and Tavily
import os

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY=os.environ.get("TAVILY_API_KEY")
OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

#Step2: Setup LLM & Tools
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

openai_llm=ChatOpenAI(model="gpt-4o-mini")
groq_llm=ChatGroq(model="llama-3.3-70b-versatile")

search_tool=TavilySearchResults(max_results=2)

#Step3: Setup AI Agent with Search tool functionality
from langgraph.prebuilt import create_react_agent
from langchain_core.messages.ai import AIMessage

system_prompt="Act as an AI chatbot who is smart and friendly"

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider=="Groq":
        llm=ChatGroq(model=llm_id)
    elif provider=="OpenAI":
        llm=ChatOpenAI(model=llm_id)

    tools=[TavilySearchResults(max_results=2)] if allow_search else []
    agent=create_react_agent(
        model=llm,
        tools=tools,
        state_modifier=system_prompt
    )
    state={"messages": query}
    response=agent.invoke(state)
    messages=response.get("messages")
    ai_messages=[message.content for message in messages if isinstance(message, AIMessage)]
    return ai_messages[-1]

