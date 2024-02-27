from typing import List
from models import DAO


class Repository:
    def __init__(self, client):
        self.client = client
        self.database = self.client["rag-demo"]

    def getAll(self) -> List[DAO]:
        corpus = self.database["corpus"]
        documents = corpus.find()
        daos = [DAO(**document) for document in documents]
        return daos
