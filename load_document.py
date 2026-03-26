from langchain_community.document_loaders import PyPDFLoader

file_path = "path/to/your/document.pdf"
loader = PyPDFLoader(file_path)
docs = loader.load()