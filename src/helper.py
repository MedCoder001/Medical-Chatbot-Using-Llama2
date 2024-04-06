from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings



# Extract the data from the PDF
def load_pdf(data_directory):
    loader = DirectoryLoader(data_directory,
                    glob="*.pdf",
                    loader_cls=PyPDFLoader)
    
    documents = loader.load()
    
    return documents



# Split the text into smaller chunks
def text_splitter(extracted_data):
    text_split = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=30)
    text_chunks = text_split.split_documents(extracted_data)
    
    return text_chunks



# Load the embeddings
def load_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
    return embeddings