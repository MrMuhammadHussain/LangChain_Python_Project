from dotenv import load_dotenv
load_dotenv()

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentType , initialize_agent , load_tools

llm = OpenAI(temperature=0.0)
llm2 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)


tools = load_tools(["wikipedia","llm-math"],llm=llm)
agent = initialize_agent(tools, llm2, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
prompt = str = input("To Search Wikipedia\n")
if prompt :
    print(agent.run(prompt))