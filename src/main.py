from extract import extract_users
from transform import enrich_users
from load import update_user


def run_pipeline():
    print("🔹 Iniciando pipeline ETL...")

    users = extract_users("data/SDW2023.csv")
    print(f"✔ {len(users)} usuários extraídos.")

    users = enrich_users(users)
    print("✔ Dados enriquecidos com IA Generativa.")

    for user in users:
        success = update_user(user)
        print(f"✔ Usuário {user['name']} atualizado? {success}")

    print("🚀 Pipeline finalizado com sucesso!")


if __name__ == "__main__":
    run_pipeline()
