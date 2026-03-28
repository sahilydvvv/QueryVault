from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from split_text import splitter

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")



vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",
)

docs = splitter
embed = vector_store.add_documents(docs)


# similar_docs = vector_store.similarity_search("your question", k=2)



# print(similar_docs)
# for doc in similar_docs:
#     print(doc.page_content)
#     print("\n---\n")