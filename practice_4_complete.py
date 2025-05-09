from dotenv import load_dotenv
import json
import os
import openai
import random

# Load environment variables from .env file
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# Create a client instance
client = openai.Client()

def get_flight_price(destination):
    # Simulate a random flight price for the given destination
    return random.randint(100, 1000)

def main():
    system_message = (
        "You are a flight reservation assistant. You can provide flight prices when the user asks for them. "
        "Use the 'get_flight_price' function to calculate the price for a given destination."
    )

    print("System message set to:", system_message)

    conversation = [
        {"role": "system", "content": system_message}
    ]

    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_flight_price",
                "description": "Calculate the price of a flight to a given destination.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination": {
                            "type": "string",
                            "description": "City e.g. Bogotá, Colombia"
                        },
                    },
                    "required": ["destination"]
                }
            }
        }
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
            tools=tools,
        )

        # Check if the response contains a function call
        if response.choices[0].finish_reason == "tool_calls":
            conversation.append(response.choices[0].message)
            tool_call = response.choices[0].message.tool_calls[0]
            if tool_call and tool_call.function.name == "get_flight_price":
                args = json.loads(tool_call.function.arguments)
                price = get_flight_price(args["destination"])
                # Append the assistant's response to the conversation
                conversation.append({"role": "tool", "tool_call_id": tool_call.id, "content": str(price)})
                # Create a new response after appending the tool result
                response = client.chat.completions.create(
                    model="gpt-4o-2024-05-13",
                    messages=conversation,
                    tools=tools,
                )
                assistant_reply = response.choices[0].message.content
                conversation.append({"role": "assistant", "content": assistant_reply})
                print("Assistant:", assistant_reply)
        else:
            assistant_reply = response.choices[0].message.content
            conversation.append({"role": "assistant", "content": assistant_reply})
            print("Assistant:", assistant_reply)

if __name__ == "__main__":
    main()