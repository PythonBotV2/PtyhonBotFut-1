import openai

#Inserir sua chave de API do OpenAI aqui
openai.api_key = "SUA_CHAVE_DE_API_AQUI"

def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()
  
texto = generate_text("Dê uma dica de aposta para o jogo entre Pachuca x Juarez")
print(texto)
