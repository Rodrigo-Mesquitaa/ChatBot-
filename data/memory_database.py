class MemoryDatabase:
    def __init__(self):
        # Um dicionário para armazenar dados de interação em memória
        self.storage = {}

    def save_data(self, key, value):
        # Armazena dados no formato chave-valor
        self.storage[key] = value

    def get_data(self, key):
        # Recupera dados a partir de uma chave
        return self.storage.get(key)

    def delete_data(self, key):
        # Remove dados associados a uma chave
        if key in self.storage:
            del self.storage[key]

    def get_all_data(self):
        # Retorna todos os dados armazenados
        return self.storage
