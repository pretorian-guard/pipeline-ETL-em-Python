import requests

API_URL = "https://sdw-2023-prd.up.railway.app"


def update_user(user: dict) -> bool:
    """
    Atualiza os dados do usuário na API.
    """
    response = requests.put(
        f"{API_URL}/users/{user['id']}",
        json=user
    )
    return response.status_code == 200
