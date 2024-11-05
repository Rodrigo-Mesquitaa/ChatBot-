def validate_input(user_input):
    # Verifica se a entrada do usuário é uma string não vazia
    return isinstance(user_input, str) and len(user_input.strip()) > 0
