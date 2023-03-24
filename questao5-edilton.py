# QUESTÃO 5 DESAFIO TARGET - EDILTON JR

# Define uma string
string = str(input("Digite a string para ser invertida: "))

# Inverte a string utilizando um loop
string_invertida = ""
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

# Imprime a string invertida
print("A string invertida é: ")
print(string_invertida)

x = input("\nAperte qualquer tecla para sair")