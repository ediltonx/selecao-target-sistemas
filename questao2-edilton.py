# QUESTÃO 2 DESAFIO TARGET - EDILTON JR

num = int(input("Digite um número: "))

fibonacci = [0, 1]
while fibonacci[-1] < num:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

if num in fibonacci:
    print(num, "pertence à sequência de Fibonacci.")
else:
    print(num, "não pertence à sequência de Fibonacci.")

x = input("\nAperte qualquer tecla para sair")