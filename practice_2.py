from dotenv import load_dotenv
import openai
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Aquí se debe configurar la clave de API de OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

# Aquí se debe crear una instancia del cliente de OpenAI

def main():
    system_message = "Eres un asistente útil."
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

        # Aquí se debe implementar la lógica para interactuar con el modelo de OpenAI con streaming

        # Procesar la respuesta del asistente y agregarla a la conversación

if __name__ == "__main__":
    main()