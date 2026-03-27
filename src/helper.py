from typing import List
from functools import lru_cache
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings

# Loader imports (new path + fallback)
try:
    from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
except ImportError:
    from langchain.document_loaders import PyPDFLoader, DirectoryLoader

# Text splitter imports (new package + fallback)
try:
    from langchain_text_splitters import RecursiveCharacterTextSplitter
except ImportError:
    from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_pdf_file(data: str) -> List[Document]:
    loader = DirectoryLoader(
        data,
        glob="*.pdf",
        loader_cls=PyPDFLoader
    )
    return loader.load()


def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    minimal_docs: List[Document] = []
    for doc in docs:
        if (doc.page_content or "").strip():
            minimal_docs.append(doc)
    return minimal_docs


def text_split(extracted_data: List[Document]) -> List[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=20
    )
    return splitter.split_documents(extracted_data)


@lru_cache(maxsize=1)
def get_embeddings() -> OpenAIEmbeddings:
    return OpenAIEmbeddings(model="text-embedding-3-small")


def download_hugging_face_embeddings() -> OpenAIEmbeddings:
    return get_embeddings()