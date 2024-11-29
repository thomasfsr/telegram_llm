from langchain.agents import AgentExecutor, create_openai_tools_agent, create_tool_calling_agent
from langchain_groq import ChatGroq
from langchain_core.prompts.chat import ChatPromptTemplate, MessagesPlaceholder

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate

from langchain_core.messages import BaseMessage, HumanMessage

from pydantic import BaseModel, Field

from langchain.output_parsers.openai_functions import JsonOutputFunctionsParser

from langchain_openai.chat_models import ChatOpenAI

from langchain_core.agents import AgentAction