from dotenv import load_dotenv
import os
import openai

# Load environment variables from .env file
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# Create a client instance
client = openai.Client()

def main():
    system_message = "You are a helpful assistant."
    print("System message set to:", system_message)

    conversation = [
        {"role": "system", "content": system_message}
    ]

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting chat. Goodbye!")
            break

        conversation.append({"role": "user", "content": user_input})

        # Correctly update to use the new API client.chat.completions.create
        response = client.chat.completions.create(
            model="gpt-4o-2024-05-13",
            messages=conversation
        )

        # Extract the assistant's reply from the response object
        assistant_reply = response.choices[0].message.content
        print("Assistant:", assistant_reply)

        conversation.append({"role": "assistant", "content": assistant_reply})

if __name__ == "__main__":
    main()