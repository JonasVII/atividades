#EXERCICIO 5
def eleitor(eleitor):
    if eleitor < 16:
        return "Não-eleitor"
    elif eleitor >=16 and eleitor < 18 or eleitor > 65:
        return "Eleitor facultativo"
    else:
        return "Eleitor obrigatório"
a = int(input("Insira a sua idade: "))
print(eleitor(a))