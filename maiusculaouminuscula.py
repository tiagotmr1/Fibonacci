def contar_a(string):
    # Converte a string para minúsculas para facilitar a contagem
    string_lower = string.lower()

    # Conta quantas vezes o caractere 'a' aparece
    contagem = string_lower.count('a')

    # Verifica se 'a' está presente na string
    if contagem > 0:
        return f"A letra 'a' aparece {contagem} vezes na string."
    else:
        return "A letra 'a' não aparece na string."

# Solicita ao usuário que informe uma string
texto = input("Digite uma string: ")

# Chama a função e exibe o resultado
print(contar_a(texto))
