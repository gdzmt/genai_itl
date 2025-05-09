from dotenv import load_dotenv
import os
import openai
import json

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Aquí se debe configurar la clave de API de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Aquí se debe crear una instancia del cliente de OpenAI

def main():
    while True:
        product_name = input("Introduce el nombre del producto (o escribe 'exit' para salir): ")
        if product_name.lower() == "exit":
            print("Saliendo. ¡Adiós!")
            break

        review = input("Introduce tu reseña para el producto: ")

        prompt = (
            "Eres un asistente útil. Basándote en la reseña del usuario, genera un objeto JSON "
            "con los siguientes campos: 'product_name', 'rating' (1-5), y 'sentiment' (positivo, neutral o negativo)."
        )

        # Aquí se debe implementar la lógica para interactuar con el modelo de OpenAI

        # Procesar la respuesta y convertirla en JSON

if __name__ == "__main__":
    main()