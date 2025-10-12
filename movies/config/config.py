from dotenv import load_dotenv
import os

load_dotenv()

class DevelopmentConfig():
    DEBUG = True
    PORT = int(os.getenv('PORT', 3000))

class DatabaseConfig():
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_NAME')
    port = int(os.getenv('DB_PORT', 3306))

config = {
    'development': DevelopmentConfig,
    'database': DatabaseConfig
}