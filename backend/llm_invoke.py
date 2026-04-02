from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from retrievers import retriever

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=None,
)

template = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful AI assistant.
Use ONLY the provided context to answer the question.
If the answer is not present in the context, say:
"I could not find the answer in the document."
"""),
    ("user", """
context: {context}
question: {question}
""")
])

while True:
    question = input("Enter your question (or 'exit' to quit): ")
    if question.lower() == 'exit':
        break

    similar_docs = retriever.invoke(question)

    if not similar_docs:
        print("No relevant documents found\n")
        continue

    context = "\n---\n".join(doc.page_content for doc in similar_docs)

    prompt = template.invoke({
        "context": context,
        "question": question
    })

    response = llm.invoke(prompt)

    print("\nAnswer:")
    print(response.content)
    