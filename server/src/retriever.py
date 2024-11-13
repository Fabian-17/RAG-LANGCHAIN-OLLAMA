from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
from src.helpers import TextActions
from src.config import env
import os

INDEX_NAME = "books"
CHROMA_DB_DIR = "chroma_db" 

class VectorDB:
    def __init__(self, chucks):
        # Verifica si el archivo ya ha sido indexado
        with open('indexed_files.txt', 'a') as file:
            pass

        with open('indexed_files.txt', 'r') as file:
            indexed_files = file.read().splitlines()

        if env.file in indexed_files:
            print(f"File {env.file} already indexed")
            # Carga el vector store de la base de datos persistente
            self._vector_store = Chroma(
                collection_name=INDEX_NAME,
                embedding_function=OllamaEmbeddings(model=env.model),
                persist_directory=CHROMA_DB_DIR
            )
            return

        # Crea y almacena el vector store de los textos, con persistencia local
        self._vector_store = Chroma.from_texts(
            texts=chucks,
            embedding=OllamaEmbeddings(model=env.model),
            collection_name=INDEX_NAME,
            persist_directory=CHROMA_DB_DIR
        )

        with open('indexed_files.txt', 'a') as file:
            file.write(env.file + '\n')

    @property
    def retriever(self):
        return self._vector_store.as_retriever()

    @property
    def vector_store(self):
        return self._vector_store

# Procesa el archivo PDF y crea los chunks
pdf_file = env.file
pdf_text = TextActions.extract_text_from_pdf(pdf_file)
chucks = TextActions.split_chucks(pdf_text, 300)

# Inicializa la base de datos de vectores
db = VectorDB(chucks=chucks)
retriever = db.retriever