import random
NumeroSorteado = random.randrange(1, 10)
NumTentivas = 3
while True:
    
    input("Informe um numero: ")
    Numero = int() 
    if Numero == NumeroSorteado:
        print("Acertoou, o numero sorteado foi: ", NumeroSorteado )
        break
    else:
        NumTentivas -=1
        if NumTentivas == 0:
            print("Tentivas esgotadas o numero sorteado", NumeroSorteado)
            break
        if Numero > NumeroSorteado:
            print("Tente um numero menor")
        else:
            print("Tente um numero maior")               
print("programa encerrado")            