import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("📘 AI Study Notes Generator")

topic = st.text_input("Enter a topic")

if st.button("Generate Notes") and topic:
    with st.spinner("Generating notes..."):
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": f"Generate simple study notes for beginners on the topic: {topic}. Use bullet points and easy language."
                }
            ]
        )

        notes = response.choices[0].message.content
        st.markdown(notes)
