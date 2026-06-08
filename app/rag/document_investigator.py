import os
import streamlit as st

from groq import Groq

from dotenv import load_dotenv

load_dotenv()


class DocumentInvestigator:

    @staticmethod
    def investigate(context):

        client = Groq(
            api_key = (
                st.secrets.get(
                    "GROQ_API_KEY",
                    os.getenv(
                        "GROQ_API_KEY"
                    )
                )
            )
        )

        prompt = f"""
You are an expert AI Data Detective.

Analyze the document context below.

Generate:

1. Executive Summary
2. Key Topics
3. Important Numbers
4. Risks
5. Recommended Actions
6. Confidence Level

Document Context:

{context}

Keep the response business-friendly.
Use markdown formatting.
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return (
            response
            .choices[0]
            .message
            .content
        )