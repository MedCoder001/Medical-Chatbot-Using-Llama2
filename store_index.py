from src.helper import load_pdf, text_splitter, load_embeddings
from langchain.vectorstores import Pinecone
import pinecone
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
PINECONE_API_ENV = os.environ.get("PINECONE_API_ENV")

# print(PINECONE_API_KEY)
# print(PINECONE_API_ENV)


extracted_data = load_pdf("data/")
text_chunks = text_splitter(extracted_data)
embeddings = load_embeddings()


# Initialize the Pinecone vector store
from pinecone import Pinecone
pc = Pinecone(
api_key = PINECONE_API_KEY,
environment = PINECONE_API_ENV    
)
index_name = "medical-chatbot"
index = pc.Index(index_name)

vectorstore = PineconeVectorStore(
    index=index,
    embedding=embeddings,
    namespace="medicalChatBot",
    index_name='medical-chatbot'
)

vectorstore.add_texts(texts=[t.page_content for t in text_chunks])