import requests

def technical_writer(text: str):
    OLLAMA_API = "http://localhost:11434/api/chat"
    HEADERS = {"Content-Type": "application/json"}
    MODEL = "llama3.2"

    messages = [
        {"role": "system",
         "content": "You are a technical software expert which wil answer questions related to software technologies and related domains with good explaination and example"},
        {"role": "user", "content": f"Please explain what this code does and why: {text}"}
    ]

    payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False
    }

    response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)
    print(response.json()['message']['content'])


input_question = input("Enter a technical question/code that you want to understand? \n")
technical_writer(input_question)