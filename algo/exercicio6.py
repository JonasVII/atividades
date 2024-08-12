#EXERCICIO 6
def numero(par):
    if par % 2 == 0:
        return "Seu número é par: 1"
    else:
        return "Seu número é ímpar: -1"
a = int(input("Informe um número: "))
print(numero(a))