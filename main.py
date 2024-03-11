#Questão 1
#Ao final do processamento, o valor da variável SOMA será 91.
"""
s  k
1  1
3  2
6  3
10 4
15 5
21 6
28 7
36 8
45 9
55 10
66 11
78 12
91 13
"""

#Questão 2
def pertence_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n

numero = int(input("Digite um número: "))
if pertence_fibonacci(numero):
    print(f"O número", numero, "pertence à Fibonacci.")
else:
    print(f"O número", numero, "não pertence à Fibonacci.")


#Questão 3
# a) 1-3-5-7-9
# b) 2-4-8-16-32-64-128
# c) 0-1-4-9-16-25-36-49
# d) 4-16-36-64-100
# e) 1-1-2-3-5-8-13
# f) Não consegui identificar.
    
#Questão 4
# Liga o 1 e o 2 interruptores, observe as lâmpadas nas salas (duas acesas e uma apagada)
# Desliga o 1 interruptor, observe as lâmpadas nas salas, a lâmpada acesa é o segundo interruptor, a lâmpada que estava apagada nas duas idas é o terceiro e a lâmpada que se apagou na segunda ida é a primeira.
    
#Questão 5
def inverter(s):
    string_invertida = ''
    for caracter in s:
        string_invertida = caracter + string_invertida
    return string_invertida

entrada = input("Digite uma string: ")
print("String invertida:", inverter(entrada))
