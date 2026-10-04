import streamlit as st
import openai
import os
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate,SystemMessagePromptTemplate,HumanMessagePromptTemplate,MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
import uuid





if "session_id" not in st.session_state:
    st.session_state["session_id"] = str(uuid.uuid4())

chat_prompt = ChatPromptTemplate.from_messages([

  ("system", 
   """You are a helpful assistant,
   Always answer the questions in english,
   Do not answer the questions in other language"""
   ),
    MessagesPlaceholder(variable_name="messages"),
   (
       "human", "{question}"
       
       )
    
    ])

def get_chat_history(session_id)->BaseChatMessageHistory:
    if session_id not in st.session_state:
        st.session_state[session_id] = ChatMessageHistory()
    return st.session_state[session_id] 
 
def genenerate_response(question,api_key,model_name,max_tokens):
    openai.api_key=api_key
    llm=ChatOpenAI(model=model_name,max_tokens=max_tokens,openai_api_key=api_key)
    output_Parser=StrOutputParser()
    chain =chat_prompt|  llm |  output_Parser
    chat_with_history = RunnableWithMessageHistory(chain,get_chat_history,input_messages_key="question",history_messages_key = "messages")
    session_id = st.session_state["session_id"]
    config = {"configurable":{"session_id":session_id}}

   
    response=chat_with_history.invoke({"question":question},config=config)
    

    return response

# Title of the app
st.title("Enhanced Q&A ChatBot With OPENAI and Langchain")

#sidebar for settings
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

# Dropdown to select various models
model_name = st.sidebar.selectbox("select the model",
                                  ["gpt-3.5-turbo",
                                   "gpt-4o",
                                   "gpt-6-luna"
                                   ])

#Adjust response parameters

max_tokens =st.sidebar.slider("select the max tokens",min_value=50,max_value=300,value=150)

# Main interface for userinput
st.write("Ask any question to the AI ChatBot")
user_question = st.text_input("You:")
if st.button("Get Response"):
    if user_question and api_key:
        with st.spinner("Generating response..."):
            answer = genenerate_response(user_question,api_key,model_name,max_tokens)
            st.write("AI ChatBot:")
            st.write(answer)
elif not api_key:
    st.warning("Please enter your OpenAI API Key in the sidebar.")
else:
    st.info("Please enter a question to get started.")  