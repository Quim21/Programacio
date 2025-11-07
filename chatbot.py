import openai

openai.api_key = "my_api_key"

def consultar_chatgpt(mensaje):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": mensaje}
        ],
        temperature=0.7
    )
    return response.choices[0].message["content"]

user_input = input("Escribe tu mensaje: ")
print(consultar_chatgpt(user_input))
