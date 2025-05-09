from dotenv import load_dotenv
import json
import os
import openai
import random

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Aquí se debe configurar la clave de API de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Aquí se debe crear una instancia del cliente de OpenAI


def get_flight_price(destination):
    # Simular un precio aleatorio para el vuelo al destino dado
    return random.randint(100, 1000)

def main():
    system_message = (
        "Eres un asistente de reservas de vuelos. Puedes proporcionar precios de vuelos cuando el usuario los solicite. "
        "Usa la función 'get_flight_price' para calcular el precio para un destino dado."
    )

    print("Mensaje del sistema configurado a:", system_message)

    conversation = [
        {"role": "system", "content": system_message}
    ]

    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "exit":
            print("Saliendo del chat. ¡Adiós!")
            break

        conversation.append({"role": "user", "content": user_input})

        # Aquí se debe implementar la lógica para interactuar con el modelo de OpenAI

        # Verificar si la respuesta contiene una llamada a función

if __name__ == "__main__":
    main()