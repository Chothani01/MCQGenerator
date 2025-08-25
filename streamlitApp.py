import os
import json 
import traceback
import pandas as pd
import streamlit as st
from src.mcqgenerator.logger import logging
from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.MCQGenerator import final_chain

with open("D:/python/DL/GenAi/Project/MCQGEN/response.json", 'r') as f:
    RESPONSE_JSON = json.load(f)
    
st.title("MCQs creator application with Langchain")

with st.form("user_input"):
    uploaded_file = st.file_uploader("Upload a PDF or txt file", type=["pdf", "txt"])
    
    # Input Field
    mcq_count = st.number_input("No. of MCQs", min_value=3, max_value=50)
    subject = st.text_input("Insert Subject", max_chars=20)
    tone = st.text_input("Complexity Level of Questions", max_chars=20, placeholder="Simple")
    button = st.form_submit_button("Create MCQs")
    
    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("loading..."):
            try:
                text = read_file(uploaded_file)
                response = final_chain.invoke(
                    {
                        "text": text,
                        "number": mcq_count,
                        "subject": subject,
                        "tone": tone,
                        "response_json": RESPONSE_JSON
                    }
                )
             
            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error("Error")
             
            else:
                if isinstance(response, dict):
                    if response is not None:
                        table_data = get_table_data(response)
                        df = pd.DataFrame(table_data)
                        st.table(df)
                    else:
                        st.error("Error is the table data")
                    
                else:
                    st.write(response)