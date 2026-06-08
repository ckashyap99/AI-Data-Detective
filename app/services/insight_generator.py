import os
import json
import streamlit as st

from groq import Groq
from dotenv import load_dotenv

load_dotenv()


class InsightGenerator:

    @staticmethod
    def generate(evidence):

        try:
            api_key = st.secrets["GROQ_API_KEY"]
        except Exception:
            api_key = os.getenv("GROQ_API_KEY")

        client = Groq(
            api_key = api_key
        )

        prompt = f"""
You are a senior data analyst.

Your job is NOT to repeat statistics.

Your job is to explain what the findings mean.

For each insight provide:

1. Observation
2. Why it matters
3. Potential business impact
4. Confidence (High/Medium/Low)

Use the evidence provided.

Do not simply restate correlation values.

Evidence:
{json.dumps(evidence, indent=2)}
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        return response.choices[0].message.content