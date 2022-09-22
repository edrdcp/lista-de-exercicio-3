print("Candidatos: \n1 - José\n2 - João\n3 - Lúcia\n4 - Benedita")
print("Entre com 0 para sair, 5 para votar nulo ou 6 para votar em branco.")
votos = 0
candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
candidato_4 = 0
nulos = 0
brancos = 0

while True:
    voto = int(input(f"Digite o voto numero {votos + 1}: "))
    if voto == 0:
        break
    votos += 1
    if voto == 1:
        candidato_1 += 1
    elif voto == 2:
        candidato_2 += 1
    elif voto == 3:
        candidato_3 += 1
    elif voto == 4:
        candidato_4 += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos += 1
    else:
        print("Voto inválido.")
        votos -= 1

porcentagem_nulos = 100 * nulos / votos
porcentagem_brancos = 100 * brancos / votos

print('Resultado')
print('José: ', candidato_1, 'votos.')
print('João: ', candidato_2, 'votos.')
print('Lúcia: ', candidato_3, 'votos.')
print('Benedita: ', candidato_4, 'votos.')
print('Nulos: ', nulos, 'votos.')
print('Brancos: ', brancos, 'votos.')
print('Porcentagem de votos Nulos: %.2f' %porcentagem_nulos, '%')
print('Porcentagem de votos Brancos: %.2f'6 %porcentagem_brancos, '%')
