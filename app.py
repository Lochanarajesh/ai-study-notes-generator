import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("📘 AI Study Notes Generator")

topic = st.text_input("Enter a topic")

if st.button("Generate Notes") and topic:
    prompt = f"""
    Generate simple study notes for beginners on the topic: {topic}.
    Use bullet points and easy language.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    notes = response.choices[0].message.content
    st.write(notes)
