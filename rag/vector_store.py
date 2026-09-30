import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


class VectorStore:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = None
        self.documents = []

    def create_index(self, documents):

        self.documents = documents

        texts = [doc["text"] for doc in documents]

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True
        )

        embeddings = np.asarray(
            embeddings,
            dtype="float32"
        )

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(embeddings)

        print(f"Added {len(documents)} chunks to FAISS.")

    def search(self, query, k=3):

        if self.index is None:
            return []

        if len(self.documents) == 0:
            return []

        query_embedding = self.model.encode(
            [query],
            convert_to_numpy=True
        )

        query_embedding = np.asarray(
            query_embedding,
            dtype="float32"
        )

        # Never ask FAISS for more results than documents available
        k = min(k, len(self.documents))

        distances, indices = self.index.search(
            query_embedding,
            k
        )

        results = []

        for index in indices[0]:

            if index >= 0 and index < len(self.documents):
                results.append(
                    self.documents[index]
                )

        return results