"""
Llama LLM neural-chat local chat interface based on Ollama https://ollama.com/download/
It enables interacting with model from terminal or another script, while
preserving chat history as context.
The module was writen following this tutorial:
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
model = OllamaLLM(model='neural-chat')
prompt = ChatPromptTemplate.from_template(template)
# chain prompt and model
chain = prompt | model

def handle_conversation(questions):
    context = f"questions: {questions}"
    print("Welcome to LLama neural-chat ChatBot. Type 'exit' to quit")

    while True:
        user_input = input("You: ")
        # exit
        if user_input.lower() == 'exit':
            break
        # else
        response = chain.invoke({"context": context, "question":user_input})
        print(f'AI chatbot: {response}\n')
        # context is history of chat
        context += f'\nUser: {user_input}\n AI: {response}'

# response = model.invoke(input='Hello')
