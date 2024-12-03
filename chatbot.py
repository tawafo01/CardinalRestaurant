import os
from confidential import api_key
from groq import Groq

def chat_with_groq(prompt, api_key):
    client = Groq(api_key=api_key)
    
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
    
    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="llama3-8b-8192", 
        )
        
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"

def chatbot_loop(api_key):
    print("Welcome to the Groq Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = chat_with_groq(user_input, api_key)
        print(f"Bot: {response}")

if __name__ == "__main__":
    # Use the API key from confidential.py
    API_KEY = api_key
    chatbot_loop(API_KEY)
