from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    DATABASE_URL: SecretStr
    API_KEY: SecretStr

    class Config:
        env_file = ".env"


settings = Settings()

print(f"database URL: {settings.DATABASE_URL}")
print(f"API key: {settings.API_KEY}")

# Безопасное использование
db_url = settings.DATABASE_URL.get_secret_value()
api_key = settings.API_KEY.get_secret_value()
