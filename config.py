import json
import os
from dotenv import load_dotenv
from datetime import timedelta

# Cargar las variables desde el archivo .env
load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)