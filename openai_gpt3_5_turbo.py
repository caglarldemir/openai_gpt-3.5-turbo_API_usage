import os
import openai
openai.organization = "YOUR_ORG_ID
openai.api_key = "YOUR API KEY"

# Use a model from OpenAI (assuming "text-embedding-ada-002" exists for this example)
model_name="gpt-3.5-turbo"

def main():
    """
    Main interaction loop for the chatbot.
    """
    print("Welcome to Chatbot! Type 'quit' to exit.")

    user_input = ""
    while user_input.lower() != "quit":
        user_input = input("You: ")

        if user_input.lower() != "quit":
            response = chat_with_openai(user_input)  # Pass user_input as an argument
            print(f"Chatbot: {response}")


def chat_with_openai(prompt):
    """
    Sends the prompt to OpenAI API using the chat interface and gets the model's response.
    """
    message = {
        'role': 'user',
        'content': prompt
    }

    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[message]
    )

    # Extract the chatbot's message from the response.
    # Assuming there's at least one response and taking the last one as the chatbot's reply.
    chatbot_response = response.choices[0].message['content']
    return chatbot_response.strip()


if __name__ == "__main__":
    main()  # This line was missing
