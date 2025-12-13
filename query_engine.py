# ===================================================
# QUERY ENGINE — TinyLlama 1.1B (Fast, Lightweight)
# ===================================================

from llama_index.core import VectorStoreIndex, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient


# Embedding model for semantic retrieval
embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

# Lightweight local language model for fast inference
llm = HuggingFaceLLM(
    model_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    tokenizer_name="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    context_window=1024,
    generate_kwargs={
        "temperature": 0.2
    }
)

# Apply global settings
Settings.embed_model = embed_model
Settings.llm = llm

# Connect to persistent Qdrant vector database
client = QdrantClient(path="vector_db/qdrant")

vector_store = QdrantVectorStore(
    client=client,
    collection_name="chips"
)

# Load existing vector index
index = VectorStoreIndex.from_vector_store(
    vector_store=vector_store,
    embed_model=embed_model
)

# Configure query engine for compact, single-pass responses
query_engine = index.as_query_engine(
    similarity_top_k=2,
    response_mode="compact"
)

def ask(question: str):
    """Returns a concise response based on the indexed datasheets."""
    return str(query_engine.query(question))


"""
# =================================================
# QUERY ENGINE — Qwen 2.5 (1.5B, Higher Accuracy)
# =================================================

from llama_index.core import VectorStoreIndex, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.huggingface import HuggingFaceLLM
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient


# Embedding model for semantic retrieval
embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

# Higher-capacity language model for improved reasoning
llm = HuggingFaceLLM(
    model_name="Qwen/Qwen2.5-1.5B-Instruct",
    tokenizer_name="Qwen/Qwen2.5-1.5B-Instruct",
    context_window=1024,
    generate_kwargs={
        "temperature": 0.2
    }
)

# Apply global settings
Settings.embed_model = embed_model
Settings.llm = llm

# Connect to persistent Qdrant vector database
client = QdrantClient(path="vector_db/qdrant")

vector_store = QdrantVectorStore(
    client=client,
    collection_name="chips"
)

# Load existing vector index
index = VectorStoreIndex.from_vector_store(
    vector_store=vector_store,
    embed_model=embed_model
)

# Configure query engine for compact, single-pass responses
query_engine = index.as_query_engine(
    similarity_top_k=2,
    response_mode="compact"
)

def ask(question: str):
    return str(query_engine.query(question))
"""
