from factory import Factory
from flask import jsonify, request

# Env
from dotenv import load_dotenv
import os

load_dotenv()

factory = Factory()
app = factory.create_app()


@app.route("/")
def main():
    query = request.args.get("query", "")
    limit = request.args.get("limit", 1)

    rag = factory.create_rag()
    output = rag.processQuery(query, limit=limit)
    # extraction = rag.processQuery("How does React Virtual DOM work?", limit=1)
    return (
        jsonify(
            {
                "answer": output.extraction.answer,
                "keywords": output.extraction.keywords,
                "sources": output.sources,
            }
        ),
        200,
    )
