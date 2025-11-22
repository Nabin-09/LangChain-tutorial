import os 
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
api_key = os.getenv("LANGSMITH_API_KEY")
tracing = os.getenv("LANGSMITH_TRACING")

file_path = './nke-10k-2023.pdf'
loader = PyPDFLoader(file_path)

docs = loader.load()

print(len(docs))