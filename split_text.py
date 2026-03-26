from langchain_text_splitters import RecursiveCharacterTextSplitter
from load_document import docs

text_splitter = RecursiveCharacterTextSplitter(chunk_size=90, chunk_overlap=25)

# splitter = text_splitter.create_documents([docs[0].page_content])
splitter = text_splitter.split_documents(docs)
# print(splitter)

# for i in splitter:
#     print(i.page_content)
#     print("\n\n")
