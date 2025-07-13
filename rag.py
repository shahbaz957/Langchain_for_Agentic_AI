import os
from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq

st.sidebar.title("**Options**")
st.sidebar.markdown("## Upload Document Here ")
uploaded_file = st.sidebar.file_uploader("Upload your document", type=["pdf", "txt", "docx"])
model_options = ["llama3-8b-8192", "llama3-70b-8192" , 'llama-3.1-8b-instant' ]
st.sidebar.markdown("### Select the Model of your Choice:")
model_name = st.sidebar.selectbox("", model_options)

# Streamlit UI
st.title("🌍 RAG GenAI App")

input_text = st.text_area("Ask any Question About Your Document : ", height=70)
if st.button("Send"):
    if input_text.strip() == "":
        st.warning("Please enter some question.")

    else:
        model = ChatGroq(model=model_name)
        
