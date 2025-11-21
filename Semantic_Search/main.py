from dotenv import load_dotenv
from langchain_core.documents import Document
import os

# Load from .env file
load_dotenv()

tracing = os.getenv("LANGSMITH_TRACING")
api_key = os.getenv("LANGSMITH_API_KEY")

print("Tracing:", tracing)
print("API Key:", api_key)
