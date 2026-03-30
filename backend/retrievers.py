from data_vectorDb import vector_store, embed


retriever = vector_store.as_retriever(
    search_type = "mmr",
    search_kwargs = {
        "k" : 4,
        "fetch_k":10,
        "lambda_mult" :0.5
    }
)

# similar_docs = retriever.invoke("")

# for doc in similar_docs:
#     print(doc.page_content)
#     print("\n---\n")

