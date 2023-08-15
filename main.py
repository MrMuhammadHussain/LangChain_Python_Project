# load API KEY from ENV
from dotenv import load_dotenv
load_dotenv()

# Langchain Lib 
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain , SimpleSequentialChain , SequentialChain
from langchain.agents import AgentType , initialize_agent , load_tools
from langchain.memory import ConversationBufferMemory

# Streamlit 
import streamlit as st

# Make LLM with Langchain and openai
llm = OpenAI(temperature=0.7,)
llm2 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
# print(llm.predict("your self"))
# Prompt Tepmlate
# prompt = PromptTemplate.from_template("Tell me about {qus}")
# print(promt.format(qus="your Self"))
# formated_Prompt = promt.format(qus="your Self")
# print(formated_Prompt)
# Streamlit Lib for UI
st.title("Article Generator") #Heading
topic = st.text_input("Topic Name")  #input Feild

title = PromptTemplate(
    input_variables = ["topic"],
    template = "Give me a Creative article title on this {topic}"
)
# formated_template = title.format(topic=topic)
body = PromptTemplate(
    input_variables = ["title"],
    template = "Write a Creative article for this title in 255 words: {title}"
)
# Chains
title_chain = LLMChain(llm=llm , prompt=title)
body_chain = LLMChain(llm=llm2 , prompt=body)



all_chain = SimpleSequentialChain(chains=[title_chain,body_chain])

if topic:
    # res = llm(formated_template)
    response = title_chain.run(topic)
    response2 = all_chain.run(topic)
    st.write(f"Title : {response.strip()}")
    st.write(response2)