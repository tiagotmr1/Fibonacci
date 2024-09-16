def is_fibonacci(num):
  # Função que calcula a sequência de Fibonacci até o número ser maior ou igual ao número informado
  fibonacci_sequence = [0, 1]

  while fibonacci_sequence[-1] < num:
      fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

  # Verifica se o número está na sequência de Fibonacci
  if num in fibonacci_sequence:
      return f"O número {num} pertence à sequência de Fibonacci."
  else:
      return f"O número {num} NÃO pertence à sequência de Fibonacci."

# Número a ser verificado
numero = int(input("Informe o número para verificar se pertence à sequência de Fibonacci: "))

# Chamada da função e exibição do resultado
print(is_fibonacci(numero))
