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
    embedding: List[float]

    def toString(self):
        codeExamples = [
            f"Example {i} in {snip.language}: \n {snip.snippet}"
            for (i, snip) in enumerate(self.codeSnippets)
        ]
        codeSnippetString = ", \n".join(codeExamples)
        return f"Title: {self.title} \n Content: {self.content} \n Code Examples: {codeSnippetString} \n More Info: {self.url}"


class Extraction(BaseModel):
    answer: str = Field(description="The concise answer to the prompt.")
    keywords: List[str] = Field(
        description="List of one or two word keywords related to the answer."
    )
