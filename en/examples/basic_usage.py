# examples/pydantic_usage.py
from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    DATABASE_URL: SecretStr
    API_KEY: SecretStr

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    def get_database_config(self):
        return {
            "url": self.DATABASE_URL.get_secret_value(),
        }

    def get_api_key(self):
        return self.API_KEY.get_secret_value()


settings = Settings()

print(f"Database URL: {settings.DATABASE_URL}")
print(f"API key: {settings.API_KEY}")

# Secure usage example
db_config = settings.get_database_config()
print(f"Database configuration: {db_config}")

api_key = settings.get_api_key()
print(f"API key (first 4 characters): {api_key[:4]}...")
