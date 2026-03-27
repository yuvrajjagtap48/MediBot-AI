from dotenv import load_dotenv
import os
from src.helper import (
    load_pdf_file,
    filter_to_minimal_docs,
    text_split,
    get_embeddings,
)
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not PINECONE_API_KEY:
    raise ValueError("Missing PINECONE_API_KEY in environment (.env).")
if not OPENAI_API_KEY:
    raise ValueError("Missing OPENAI_API_KEY in environment (.env).")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

extracted_data = load_pdf_file(data="data/")
filter_data = filter_to_minimal_docs(extracted_data)
text_chunks = text_split(filter_data)

embeddings = get_embeddings()

pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medical-chatbot"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(cloud="aws", region="us-east-1"),
    )

PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings,
)