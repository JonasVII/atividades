#EXERCICIO 7
def fatorial(f):
    if f <= 0:
       return "insira um número valido" 
        
    else:
        a = 1
        b = 0
        for i in range(f):
            b=b+1
            a=a*b
        return (a)
f = int(input("Insira um número: "))
print(fatorial(f))