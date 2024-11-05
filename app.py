import streamlit as st
from chatbot.chatbot_agent import ChatbotAgent
from chatbot.interaction_manager import InteractionManager

st.title("Chatbot Interativo com Aprendizado Contínuo")
chatbot_agent = ChatbotAgent()
interaction_manager = InteractionManager(chatbot_agent)

user_input = st.text_input("Você: ")
if st.button("Enviar"):
    if user_input:
        response = interaction_manager.process_interaction(user_input)
        st.write("Chatbot:", response)
    else:
        st.warning("Digite algo para receber uma resposta.")
