import pandas as pd
import requests

API_URL = "https://sdw-2023-prd.up.railway.app"


def load_user_ids(csv_path: str) -> list:
    """
    Lê o arquivo CSV e retorna uma lista de IDs de usuários.
    """
    df = pd.read_csv(csv_path)
    return df["UserID"].tolist()


def get_user(user_id: int) -> dict | None:
    """
    Consome a API para buscar os dados de um usuário.
    """
    response = requests.get(f"{API_URL}/users/{user_id}")
    if response.status_code == 200:
        return response.json()
    return None


def extract_users(csv_path: str) -> list:
    """
    Pipeline de extração completo.
    """
    user_ids = load_user_ids(csv_path)
    users = []

    for user_id in user_ids:
        user = get_user(user_id)
        if user:
            users.append(user)

    return users
