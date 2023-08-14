from dotenv import load_dotenv
load_dotenv()

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain , SimpleSequentialChain , SequentialChain
from langchain.agents import AgentType , initialize_agent , load_tools
from langchain.memory import ConversationBufferMemory


llm = OpenAI(temperature=0)
# print(llm.predict("your self"))

promt = PromptTemplate.from_template("Tell me about {qus}")
# print(promt.format(qus="your Self"))
formated_Promt = promt.format(qus="your Self")
# print(formated_Promt)