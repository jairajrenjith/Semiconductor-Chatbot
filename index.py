import os
import json

from llama_index.core import Document, VectorStoreIndex, StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

# Directory containing processed JSON chunks
PROCESSED_DIR = "data/processed"

# Initialize the embedding model
embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

# Initialize a persistent local Qdrant vector database
client = QdrantClient(path="vector_db/qdrant")

vector_store = QdrantVectorStore(
    client=client,
    collection_name="chips"
)

documents = []

# Load processed JSON data and convert to LlamaIndex Documents
for file in os.listdir(PROCESSED_DIR):
    if file.endswith(".json"):
        with open(os.path.join(PROCESSED_DIR, file), "r", encoding="utf-8") as f:
            chunks = json.load(f)
            for chunk in chunks:
                documents.append(
                    Document(
                        text=chunk["text"],
                        metadata={
                            "source": chunk.get("source", file),
                            "page": chunk.get("page", "unknown")
                        }
                    )
                )

# Bind the vector store to the storage context
storage_context = StorageContext.from_defaults(
    vector_store=vector_store
)

# Create and persist the vector index
VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context,
    embed_model=embed_model
)

print("Vector database created and persisted.")

client.close()
