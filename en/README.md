# Security and Best Practices for Working with .env

## What is .env?

The .env file is a simple text file used to store the project's environment variables. These files are particularly useful for managing configuration settings and sensitive information such as API keys, database credentials, and other secrets.

## Why was .env created?

The concept of the .env file was popularized by the Twelve-Factor App methodology, which emphasizes the importance of storing configuration in the environment. It was created to address several key issues:

1. **Security**: Storing sensitive information outside of the source code repository.
2. **Flexibility**: Easily changing configuration between different environments (development, testing, production).
3. **Simplicity**: Providing a straightforward way to manage environment-dependent settings.

## Best Practices

For a complete list of best practices, see [BEST_PRACTICES.md](./BEST_PRACTICES.md).

## Examples

### Basic Usage

```python
# examples/basic_usage.py
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')

print(f"Database URL: {DATABASE_URL}")
print(f"API Key: {API_KEY}")
```

See the code examples in the [examples](./examples) directory.

## Additional Resources

- [The Twelve-Factor App](http://12factor.net/)
- [python-dotenv Documentation](https://github.com/theskumar/python-dotenv)
- [OWASP Secure Headers Guide](https://owasp.org/www-project-secure-headers/)
