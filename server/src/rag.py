from typing import List
from dotenv import load_dotenv
import os

load_dotenv()

from pydantic import BaseModel, Field


class CodeSnippet(BaseModel):
    snippet: str
    language: str


class DAO(BaseModel):
    id: str
    title: str
    url: str
    content: str
    codeSnippets: List[CodeSnippet]


class RAGService:
    def __init__(self):
        pass
