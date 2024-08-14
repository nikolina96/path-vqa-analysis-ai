"""
Llama LLM llama3.1 local chat interface based on Ollama https://ollama.com/download/
It enables interaction with a model from the terminal or another script, while
preserving chat history as context.
The module was written following this tutorial:
https://www.youtube.com/watch?v=d0o89z134CQ
"""

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the conversation history {context}

Question: {question}

Answer:
"""
model = OllamaLLM(model='llama3.1')
prompt = ChatPromptTemplate.from_template(template)
# chain prompt and model
chain = prompt | model

def handle_conversation(data):
    context = f"data: {data}"
    print("Welcome to LLama ChatBot. Type 'exit' to quit")

    while True:
        user_input = input("You: ")
        # exit
        if user_input.lower() == 'exit':
            break
        # else
        response = chain.invoke({"context": context, "question":user_input})
        print(f'\nAI chatbot: {response}\n')
        # context is history of chat
        context += f'\nUser: {user_input}\n AI: {response}'
    return context[len(f"data: {data}"):]

# response = model.invoke(input='Hello')
