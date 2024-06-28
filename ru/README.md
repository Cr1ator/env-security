# Безопасность и лучшие практики работы с .env

## Что такое .env?

Файл .env - это простой текстовый файл, используемый для хранения переменных окружения проекта. Эти файлы особенно полезны для управления настройками конфигурации и конфиденциальной информацией, такой как API-ключи, учетные данные базы данных и другие секреты.

## Зачем был создан .env?

Концепция .env файла была популяризирована методологией Twelve-Factor App, которая подчеркивает важность хранения конфигурации в окружении. Он был создан для решения нескольких ключевых проблем:

1. **Безопасность**: Хранение конфиденциальной информации вне репозитория исходного кода.
2. **Гибкость**: Возможность легко менять конфигурацию между различными средами (разработка, тестирование, продакшн).
3. **Простота**: Предоставление простого способа управления настройками, зависящими от окружения.

## Лучшие практики

Полный список лучших практик приведен в [BEST_PRACTICES.md](./BEST_PRACTICES.md).

## Примеры

### Базовое использование

```python
# examples/basic_usage.py
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')

print(f"URL базы данных: {DATABASE_URL}")
print(f"API ключ: {API_KEY}")
```

Примеры кода смотрите в каталоге [examples](./examples).

## Дополнительные ресурсы

- [Приложение с двенадцатью факторами](http://12factor.net/)
- [Документация по python-dotenv](https://github.com/theskumar/python-dotenv)
- [Руководство по безопасной настройке OWASP](https://owasp.org/www-project-secure-headers/)