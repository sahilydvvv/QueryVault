from langchain_community.document_loaders import PyPDFLoader

file_path = "C:\\Users\\sahil\\Desktop\\resume final.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()
# print(docs[0].page_content)