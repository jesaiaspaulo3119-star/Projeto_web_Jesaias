''' Calculando Notas'''
contador=1
soma=0
while contador <= 3:
    nota=float(input(f"Digite A{contador} nota: "))
    soma=soma + nota
    contador+=1
    media=soma/3
    print(f"Media: {media}")