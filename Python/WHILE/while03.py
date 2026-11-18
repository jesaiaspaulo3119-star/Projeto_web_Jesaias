''' Calculando Notas'''
contador=1
soma=0
while contador <= 3:
    nota=float(input(f"Digite a{contador} nota: "))
    soma=soma + nota
    media=nota/3
    print(f"Media: {media}")