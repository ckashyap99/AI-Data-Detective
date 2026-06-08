import os
import streamlit as st

from groq import Groq

from dotenv import load_dotenv

load_dotenv()


class QAEngine:

    @staticmethod
    def answer_question(
        question,
        context
    ):
        try:
            api_key = st.secrets["GROQ_API_KEY"]
        except Exception:
            api_key = os.getenv("GROQ_API_KEY")

        client = Groq(
            api_key = api_key
                
        )

        prompt = f"""
You are an expert document analyst.

Answer ONLY using the provided context.

If the answer cannot be found in the context,
say:

'The document does not provide enough information.'

Context:

{context}

Question:

{question}
"""

        response = (
            client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.1
            )
        )

        return (
            response
            .choices[0]
            .message
            .content
        )