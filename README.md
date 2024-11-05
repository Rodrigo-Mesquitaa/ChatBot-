configurar e executar o projeto.

markdown
Copiar código
# Chatbot Interativo com Aprendizado Contínuo

## Descrição
Este projeto implementa um chatbot que aprende e se adapta com base nas interações do usuário, 
armazenando dados relevantes de forma contínua.

# Estrutura do projeto 

chatbot_project/
- │
- ├── .env                        # Arquivo de variáveis de ambiente
- ├── Dockerfile                  # Dockerfile para a imagem Docker
- ├── README.md                   # Documentação do projeto
- ├── requirements.txt            # Lista de dependências do projeto
- ├── main.py                     # Script principal para linha de comando
- ├── app.py                      # Interface Streamlit
- │
- ├── config/
- │   ├── __init__.py             # Torna config um módulo
- │   └── config.py               # Configurações do projeto
- │
- ├── data/
- │   ├── __init__.py             # Torna data um módulo
- │   ├── memory_database.py      # Banco de dados em memória
- │
- ├── chatbot/
- │   ├── __init__.py             # Torna chatbot um módulo
- │   ├── chatbot_agent.py        # Lógica do chatbot
- │   ├── interaction_manager.py  # Gerenciamento das interações
- │
- └── utils/
    ├── __init__.py             # Torna utils um módulo
    ├── helpers.py              # Funções auxiliares
    └── logger.py               # Configuração de log


## Requisitos
- Python 3.9+
- Docker (opcional)

## Instalação

1. Clone o repositório:
   ```bash
   git clone <repo-url>

## Crie um ambiente virtual e instale as dependências:

bash
Copiar código
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Defina a chave da API do LLM em .env.
Executando a Aplicação.

## Interface de Linha de Comando:
```bash
Copiar código
python main.py

## Interface Web (Streamlit):
```bash
Copiar código
streamlit run app.py


## Docker:
``` bash
Copiar código
docker build -t chatbot_app .
docker run -p 8501:8501 chatbot_app
Essas instruções cobrem toda a criação do projeto, incluindo uma estrutura completa e modular, 
armazenamento em memória e execução em contêiner Docker.