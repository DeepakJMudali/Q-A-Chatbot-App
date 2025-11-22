import streamlit as st
import openai
import os
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate

from dotenv import load_dotenv

load_dotenv()

# #Langsmith tracking
# os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
# os.environ["LangCHAIN_PROJECT_NAME"] = "Q&A ChatBot With OPENAI"

#Prompt Template
system_template = "You are a helpful AI assistant. Please response to the user queries."
human_template = "{question}" 

system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

chat_prompt = ChatPromptTemplate.from_messages([

  system_message_prompt,  human_message_prompt
    
    ])
 
def genenerate_response(question,api_key,model_name,temperature,max_tokens):
    openai.api_key=api_key
    llm=ChatOpenAI(model=model_name,temperature=temperature,max_tokens=max_tokens,openai_api_key=api_key)
    output_Parser=StrOutputParser()
    chain =chat_prompt|  llm |  output_Parser
    response=chain.invoke({"question":question})
    return response

# Title of the app
st.title("Enhanced Q&A ChatBot With OPENAI and Langchain")

#sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

# Dropdown to select various models
model_name = st.sidebar.selectbox("select the model",
                                  ["gpt-3.5-turbo",
                                   "gpt-4o"
                                   ])

#Adjust response parameters
temperature = st.sidebar.slider("select the temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens =st.sidebar.slider("select the max tokens",min_value=50,max_value=300,value=150)

# Main interface for userinput
st.write("Ask any question to the AI ChatBot")
user_question = st.text_input("You:")
if user_question and api_key:
    with st.spinner("Generating response..."):
        answer = genenerate_response(user_question,api_key,model_name,temperature,max_tokens)
        st.write("AI ChatBot:")
        st.write(answer)
elif not api_key:
    st.warning("Please enter your OpenAI API Key in the sidebar.")
else:

    st.info("Please enter a question to get started.")  

