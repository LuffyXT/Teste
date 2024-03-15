def verifica_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        return f"{numero} pertence à sequência de Fibonacci."
    else:
        return f"{numero} não pertence à sequência de Fibonacci."

numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
print(verifica_fibonacci(numero))