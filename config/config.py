import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

class Config:
    LLM_API_KEY = os.getenv("LLM_API_KEY")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
