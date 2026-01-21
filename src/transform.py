import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")


def generate_ai_news(user: dict) -> str:
    """
    Gera uma mensagem personalizada utilizando IA Generativa.
    """
    completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "Você é um especialista em marketing bancário."
            },
            {
                "role": "user",
                "content": (
                    f"Crie uma mensagem curta (máx. 100 caracteres) "
                    f"para {user['name']} sobre a importância dos investimentos."
                )
            }
        ]
    )

    return completion.choices[0].message.content.strip()


def enrich_users(users: list) -> list:
    """
    Enriquecimento dos dados com mensagens geradas por IA.
    """
    for user in users:
        news = generate_ai_news(user)
        user["news"].append({
            "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
            "description": news
        })
    return users
