from fastapi import FastAPI
from fastapi.responses import JSONResponse  
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins= ['http://localhost:5173'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

file_path = './nke-10k-2023.pdf'
loader = PyPDFLoader(file_path)
docs = loader.load()

@app.get('/')
def home(): 
    return {'message' : 'This is home'}


@app.get('/pdfdata')
def get_data(page:int = 0):
    doc = docs[page]
    return{
        'page_content' : doc.page_content,
        'metadata' : doc.metadata,
        'total_pages' : len(docs)
    }

