#EXERCICIO 4
def conceito(aulas,qt_presença,nota):
    presença = aulas - qt_presença
    presença_aulas = presença/aulas

    if nota < 0 or nota > 10:
        return "nota invalida"
    elif qt_presença < 0 or aulas < 0:
        return "quantidade de faltas ou aulas invalidas"
    elif qt_presença > aulas:
        return "quantidade de faltas invalidas"
    if presença_aulas < 0.25 or nota < 6:
        return 0
    else:
        return 1

a = int(input("insira a quantidade de aulas: "))
b = int(input("insira a quantidade de faltas: "))
c = float(input("insira a nota: "))
print(conceito(a,b,c))
