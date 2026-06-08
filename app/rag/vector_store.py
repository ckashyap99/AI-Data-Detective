import chromadb

from sentence_transformers import (
    SentenceTransformer
)


class VectorStore:

    def __init__(self):

        self.client = (
            chromadb.PersistentClient(
                path="data/chroma_db"
            )
        )

        self.collection = (
            self.client.get_or_create_collection(
                name="document_collection"
            )
        )

        self.embedding_model = (
            SentenceTransformer(
                "all-MiniLM-L6-v2"
            )
        )

    def index_chunks(self, chunks):

        # Clear previous document

        if self.collection.count() > 0:

            existing = (
                self.collection.get()
            )

            self.collection.delete(
                ids=existing["ids"]
            )

        embeddings = (
            self.embedding_model.encode(
                chunks
            ).tolist()
        )

        ids = [
            f"chunk_{i}"
            for i in range(
                len(chunks)
            )
        ]

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings
        )

    def search(
        self,
        query,
        top_k=5
    ):

        query_embedding = (
            self.embedding_model.encode(
                query
            ).tolist()
        )

        results = (
            self.collection.query(
                query_embeddings=[
                    query_embedding
                ],
                n_results=top_k
            )
        )

        return results