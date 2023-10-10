def escrever_votos(votos):
    with open('votos.txt', 'w') as arquivo:
        for voto in votos:
            arquivo.write(str(voto) + '\n')

def ler_votos():
    votos = []
    with open('votos.txt', 'r') as arquivo:
        for linha in arquivo:
            votos.append(int(linha))
    return votos



def main():
    votos_bart = 0
    votos_homer = 0
    votos_nulos = 0

    votos = []

    while len(votos) < 5:
        voto = int(input(f'Voto da pessoa {len(votos)}: Digite 1 para Bart, 2 para Homer: '))
        if voto == 1:
            votos.append(voto)
            votos_homer +=1
        elif voto == 2:
            votos.append(voto)
            votos_bart +=1
        else:
            print('Voto invalido, digite apenas 1 ou 2!')
            votos_nulos+=1

    escrever_votos(votos)
    votos_apurados = ler_votos()
    voto = votos_apurados

    print(f'Resultados da votação:')
    print(f'Bart teve {votos_bart} votos.')
    print(f'Homer teve {votos_homer} votos.')

    if votos_bart > votos_homer:
        print('Bart foi o personagem mais votado.')
    elif votos_homer > votos_bart:
        print('Homer foi o personagem mais votado.')
    else:
        print('Houve um empate entre Bart e Homer.')

    print(f'Total de votos nulos: {votos_nulos}')


main()