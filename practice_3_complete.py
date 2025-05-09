from dotenv import load_dotenv
import os
import openai
import json

# Load environment variables from .env file
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

# Create a client instance
client = openai.Client()

def main():

    while True:
        product_name = input("Enter the product name (or type 'exit' to quit): ")
        if product_name.lower() == "exit":
            print("Exiting. Goodbye!")
            break

        review = input("Enter your review for the product: ")

        prompt = (
            "You are a helpful assistant. Based on the user's review, generate a JSON object "
            "with the following fields: 'product_name', 'rating' (1-5), and 'sentiment' (positive, neutral, or negative)."
        )

        # Correctly update to use the new API client.chat.completions.create
        response = client.chat.completions.create(
            model="gpt-4o-2024-05-13",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": f"Product: {product_name}\nReview: {review}"}
            ]
        )

        # Access the response content correctly
        json_output = response.choices[0].message.content
        try:
            parsed_json = json.loads(json_output)
            print("Generated JSON:", json.dumps(parsed_json, indent=4))
        except json.JSONDecodeError:
            print("Failed to parse JSON. Response was:", json_output)

if __name__ == "__main__":
    main()