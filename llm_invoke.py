from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from load_document import docs

template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. summarize the following document in one line."),
    ("user", "{input}")
])

prompt = template.invoke({
    "input": f"Answer the question based on the following document: {docs[0].page_content}"
})

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=None,
)

response = llm.invoke(prompt)
print(response.content)