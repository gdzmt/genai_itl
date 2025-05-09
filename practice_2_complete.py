from dotenv import load_dotenv
import os
import openai

# Load environment variables from .env file
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# Create a client instance
client = openai.Client()

def main():
    # Set the system message for the assistant
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
            messages=conversation,
            stream=True
        )

        print("Assistant:", end=" ")
        assistant_response = ""
        for chunk in response:
            content = chunk.choices[0].delta.content
            if content:  # Ensure content is not None
                print(content, end="", flush=True)
                assistant_response += content
        print()  # Ensure a newline after the assistant's response

        conversation.append({"role": "assistant", "content": assistant_response})

if __name__ == "__main__":
    main()