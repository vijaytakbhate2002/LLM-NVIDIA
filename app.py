from openai import OpenAI
import streamlit as st
import re
from dotenv import load_dotenv
import os

load_dotenv() 
secret_key = os.getenv("SECRET_KEY")



st.header("GPT - Powred with (NVIDIA/llama-3.1)", divider='rainbow')

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = secret_key # use your API KEY
)

user_input = st.text_area("Ask me anything...")

if len(user_input) > 1:
    try:
        completion = client.chat.completions.create(
        model="nvidia/llama-3.1-nemotron-70b-instruct",
        messages=[{"role":"user","content":user_input}],
        temperature=0.5,
        top_p=1,
        max_tokens=1024,
        stream=True
        )

        output = """"""

        for chunk in completion:
            if chunk.choices[0].delta.content is not None:
                output += " " + chunk.choices[0].delta.content

        def clean_text(text):
            text = re.sub(r'\s+', ' ', text).strip()
            text = re.sub(r'[^a-zA-Z0-9.,!?\'\"\s]', '', text)
            return text
        
        st.markdown(clean_text(output))
    except:
        st.error("API Time out")
    