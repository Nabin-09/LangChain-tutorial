from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader    
import os

# Load from .env file
load_dotenv()

tracing = os.getenv("LANGSMITH_TRACING")
api_key = os.getenv("LANGSMITH_API_KEY")

print("Tracing:", tracing)
print("API Key:", api_key)

# this was to load the pdf


documents = [
    Document(
        page_content="Dogs are great companions, known for their loyalty and friendliness.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Cats are independent pets that often enjoy their own space.",
        metadata={"source": "mammal-pets-doc"},
    ),
]