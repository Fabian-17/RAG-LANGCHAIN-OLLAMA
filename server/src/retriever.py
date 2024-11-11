from langchain_chroma import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from src.helpers import TextActions
from src.config import env
import chromadb

INDEX_NAME="books"
chroma_client = chromadb.HttpClient(host='localhost', port=8000)

class VectorDB:
    def __init__(self, chucks):

        with open('indexed_files.txt', 'a') as file:
            pass

        with open('indexed_files.txt', 'r') as file:
            indexed_files = file.read().splitlines()

        if env.file in indexed_files:
            print(f"File {env.file} already indexed")

            # create _vector_store but don't index
            self._vector_store = Chroma(
                client=chroma_client,
                collection_name=INDEX_NAME,
                embedding_function=OllamaEmbeddings(
                    model=env.model,
                ),
            )

            return

        self._vector_store = Chroma.from_texts(
            texts=chucks,
            embedding=OllamaEmbeddings(
                model=env.model,
            ),
            client=chroma_client,
            collection_name=INDEX_NAME
        )

        with open('indexed_files.txt', 'a') as file:
            file.write(env.file + '\n')
        

    @property
    def retriever(self):
        return self._vector_store.as_retriever()
    
    @property
    def vector_store(self):
        return self._vector_store

pdf_file = env.file
pdf_text = TextActions.extract_text_from_pdf(pdf_file)

chucks = TextActions.split_chucks(pdf_text, 300)

db = VectorDB(chucks=chucks)

retriever = db.retriever