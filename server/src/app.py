from factory import Factory
from flask import jsonify

# Env
from dotenv import load_dotenv
import os

load_dotenv()

factory = Factory()
app = factory.create_app()


@app.route("/")
def main():
    repo = factory.create_repo()
    print(repo.getAll())
    return jsonify({"msg": "Hello World"}), 200
