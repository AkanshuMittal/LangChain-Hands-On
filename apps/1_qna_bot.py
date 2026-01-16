from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

st.title("AskBuddy - AI Qna Bot")
st.markdown("My Qna Bot with Langchain and Google Gemini !")

if "messages" not in st.session_state:
      st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content=message["content"]
    st.chat_message(role).markdown(content)
    
query = st.chat_input("Ask Anyhting?")
if query:
    st.session_state.messages.append({"role":"user", "content": query})
    st.chat_message("user").markdown(query)
    result = llm.invoke(query)
    st.chat_message("ai").markdown(result.content)
    st.session_state.messages.append({"role": "ai", "content": result.content})

# while True:
#     query = input("User: ")

#     if query.lower() in ["quit","bye","exit"]:
#         print("GoodBye")
#         break

#     result = llm.invoke(query)

#     print("AI: ", result.content, "\n")


