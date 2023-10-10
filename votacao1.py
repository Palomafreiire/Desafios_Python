import os
# Função para limpar a tela

def limpar_tela():
    if os.name == 'posix':
        os.system('clear')
    elif os.name =='nt':
        os.system('cls')

votos_bart = 0
votos_homer = 0
votos_invalido = 0

while votos_bart+votos_homer < 5:
    voto = int( input(f'Qual o seu personagem de "The simpsons" favorito  \n Digite 1 se você vota no Bart: \n Digite 2 se você vota no Homer: '))
    if voto == 1:
        print('Você está votando no Bart')
        votos_bart +=1
    elif voto == 2:
        print('Você está votando no Homer')
        votos_homer +=1
    else:
        print('voto invalido, digite apenas 1 ou 2')
        votos_invalido +=1
        
limpar_tela()
    
print(f'Total para Bart: {votos_bart} votos \nTotal para Homer {votos_homer} votos ')
print(f'total votos invalido {votos_invalido}')

if votos_homer > votos_bart:
    print('Homer teve mais votos')
elif votos_bart > votos_homer:
    print('Bart teve mais votos')
elif votos_homer == votos_bart:
    print('Empatou!!')
else:
    pass

    

    