from chatbot.chatbot_agent import ChatbotAgent
from chatbot.interaction_manager import InteractionManager
from utils.helpers import validate_input

def main():
    chatbot_agent = ChatbotAgent()
    interaction_manager = InteractionManager(chatbot_agent)
    
    print("Bem-vindo ao Chatbot Interativo! Digite 'sair' para encerrar.")

    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            break
        if validate_input(user_input):
            response = interaction_manager.process_interaction(user_input)
            print("Chatbot:", response)
        else:
            print("Entrada inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
