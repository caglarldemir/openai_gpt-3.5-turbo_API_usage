import os
import openai

# Set your OpenAI credentials
openai.api_key = os.getenv("OPENAI_API_KEY")  # Recommended way
openai.organization = os.getenv("OPENAI_ORG_ID")  # Optional

# Model selection
model_name = "gpt-3.5-turbo"  # or "gpt-4o", "gpt-4", etc.

def chat_with_openai(prompt):
    """
    Sends the prompt to OpenAI API using the chat interface and gets the model's response.
    """
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    chatbot_response = response.choices[0].message.content
    return chatbot_response.strip()

def main():
    """
    Main interaction loop for the chatbot.
    """
    print("Welcome to Chatbot! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "quit":
            print("Goodbye!")
            break
        response = chat_with_openai(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
