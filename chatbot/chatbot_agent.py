import os
from langchain import LangChain
from config.config import Config
from utils.logger import get_logger

class ChatbotAgent:
    def __init__(self):
        self.llm_api_key = Config.LLM_API_KEY
        self.lang_chain = LangChain(api_key=self.llm_api_key)
        self.logger = get_logger(self.__class__.__name__)

    def respond(self, user_input):
        try:
            # Gera resposta usando LangChain
            response = self.lang_chain.generate(user_input)
            self.logger.info(f"Resposta gerada: {response}")
            return response
        except Exception as e:
            # Log de erro
            self.logger.error(f"Erro ao gerar resposta: {e}")
            return "Desculpe, ocorreu um erro ao processar sua solicitação."
