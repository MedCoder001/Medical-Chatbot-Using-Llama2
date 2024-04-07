from flask import Flask, render_template, request, jsonify
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.llms import CTransformers
from dotenv import load_dotenv
from src.helper import load_embeddings
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")

# Initialize the Pinecone vector store
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medical-chatbot"

# Load the embeddings
embeddings = load_embeddings()

# Load the index
vectorstore = PineconeVectorStore(
    index_name=index_name,
    embedding=embeddings,
    namespace="medicalChatBot"
)

PROMPT = PromptTemplate(template=prompt_template,
                        input_variables=["context", "question"])
chain_type_kwargs = {"prompt": PROMPT}

llm = CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                    model_type="llama",
                    config={"max_new_tokens": 512,
                            "temperature": 0.8})

qa = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 2}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs,
    chain_type="stuff"
)

@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print("Input: ", input)
    result = qa.invoke({"query": input})
    print("Response: ", result["result"])
    return str(result["result"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
