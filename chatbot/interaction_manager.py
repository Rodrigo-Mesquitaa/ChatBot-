from data.memory_database import MemoryDatabase
from utils.logger import get_logger

class InteractionManager:
    def __init__(self, chatbot_agent):
        self.database = MemoryDatabase()
        self.chatbot_agent = chatbot_agent
        self.logger = get_logger(self.__class__.__name__)

    def process_interaction(self, user_input):
        # Log da interação do usuário
        self.logger.debug(f"Processando interação: {user_input}")
        
        # Gera a resposta do chatbot
        response = self.chatbot_agent.respond(user_input)
        
        # Armazena a interação no banco de dados
        self.database.save_data(user_input, response)
        
        # Retorna a resposta gerada
        return response
