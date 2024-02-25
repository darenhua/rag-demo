from typing import List

from pydantic import BaseModel, Field


class CodeSnippet(BaseModel):
    snippet: str
    language: str


class DAO(BaseModel):
    _id: str
    title: str
    url: str
    content: str
    codeSnippets: List[CodeSnippet]


class Repository:
    def __init__(self, client):
        self.client = client
        self.database = self.client["rag-demo"]

    def getAll(self) -> List[DAO]:
        corpus = self.database["corpus"]
        documents = corpus.find()
        daos = [DAO(**document) for document in documents]
        return daos
