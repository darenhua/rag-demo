import numpy as np
from numpy.linalg import norm

from typing import List
from dotenv import load_dotenv

load_dotenv()

from pydantic import BaseModel
from models import DAO, Extraction


class SimilarDocument(BaseModel):
    document: DAO
    similarityScore: float


class RAGOutput(BaseModel):
    extraction: Extraction
    sources: List[str]


class RAGService:
    def __init__(self, repositoryService, completionService):
        self.repository = repositoryService
        self.completion = completionService
        self.documents = repositoryService.getAll()

    def retrieveDocuments(self, queryEmbedding, limit=2) -> List[SimilarDocument]:
        similarities = [
            SimilarDocument(
                document=doc,
                similarityScore=self.cosineSimilarity(
                    np.array(queryEmbedding), np.array(doc.embedding)
                ),
            )
            for doc in self.documents
        ]
        sortedDocs = sorted(similarities, key=lambda x: x.similarityScore, reverse=True)
        print("Retrieved Docs: ", [doc.document.title for doc in sortedDocs])
        chosenDocs = sortedDocs[:limit]
        print("Chosen Docs: ", [doc.document.title for doc in sortedDocs])
        return chosenDocs

    def generateResponse(self, query: str, retrievedDocs: List[SimilarDocument]) -> str:
        context = " ".join(
            [doc.document.content for doc in retrievedDocs]
        )  # TODO: Many improvements here!
        response = self.completion.getCompletion(query, context)
        print("RAG Response", response)
        return response

    def processQuery(self, query: str, limit=2) -> str:
        embedding = self.completion.getEmbeddings(query)
        chosenDocs = self.retrieveDocuments(embedding, limit=limit)
        extraction: Extraction = self.generateResponse(query, chosenDocs)
        sources: List[str] = [doc.document.url for doc in chosenDocs]
        return RAGOutput(extraction=extraction, sources=sources)

    def cosineSimilarity(self, A, B):
        return np.dot(A, B) / (norm(A) * norm(B))

    # def DAOtoEmbedding(self):
    #     for doc in self.documents:
    #         stringRep = doc.toString()
    #         self.completion.getEmbeddings(stringRep)
    #         # Push to DB
    #     return
