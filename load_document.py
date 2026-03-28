from langchain_community.document_loaders import PyPDFLoader

file_path = "./docs/sample.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()
# print(docs[0].page_content)