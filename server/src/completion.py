from typing import List
from dotenv import load_dotenv
import os

load_dotenv()

from pydantic import BaseModel, Field


class Extraction(BaseModel):
    answer: str = Field(description="The concise answer to the prompt.")
    keywords: List[str] = Field(
        description="List of one or two word keywords related to the answer."
    )


class CompletionService:
    def __init__(self, client):
        self.client = client

    def getCompletion(self, prompt: str, context: str) -> Extraction:
        content = f"CONTEXT: {context} PROMPT: {prompt}"

        # Using OpenAI Function Calling to make sure output is in the form Extraction.
        return self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            response_model=Extraction,
            max_retries=3,
            messages=[
                {
                    "role": "system",
                    "content": "Your role is to answer the prompt using the context given to in a clear and concise manner.",
                },
                {"role": "user", "content": content},
            ],
        )
