from dotenv import load_dotenv
import os

load_dotenv()

class DevelopmentConfig():
    DEBUG=True
    PORT=os.getenv('PORT', 5002)

class DatabaseConfig():
    host = os.getenv('DB_HOST')
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    database = os.getenv('DB_NAME')

config = {
    'development': DevelopmentConfig,
    'database': DatabaseConfig
}