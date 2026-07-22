from pathlib import Path

from src.data_loader import load_all_documents
from src.embedding import EmbeddingPipeline
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch


# langgraph/4-RAG/data ==> folder
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

## Example Usage
if __name__ == "__main__":
    docs = load_all_documents(str(DATA_DIR)) # Step 1

    # # Step 2 -> Embedding
    # chunks = EmbeddingPipeline().chunk_documents(docs)
    # chunk_vector = EmbeddingPipeline().embed_chunks(chunks=chunks)

    store = FaissVectorStore("faiss_store")
    store.build_from_documents(documents=docs)
    store.load()
    # print(store.query("What is Lesson RAG", top_k=3))

    rag_search = RAGSearch()
    query = "What is Lesson RAG"
    summary = rag_search.search_and_summarize(query=query, top_k=3)

    print("summary: ", summary)
    # print(chunk_vector)
