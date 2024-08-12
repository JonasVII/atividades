#EXERCICIO 3
def conceito(n):
    if n>=9 and n<=10:
        return "A"
    elif n>=8 and n<9:
        return "B"
    elif n>=7 and n<8:
        return "C"
    elif n>=6 and n<7:
        return "D"
    elif n < 6:
        return "F"
    else:
        return "nota invalida"
        
a = float(input("informe a nota: "))
print(conceito(a))