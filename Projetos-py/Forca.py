import random

# Lista de palavras
palavras = ['python', 'programacao', 'jogo', 'forca', 'aleatorio', 'vida', 'chances', 'jogador', 'perder', 'letra']

def jogar_forca():
    palavra_secreta = random.choice(palavras)
    vidas = 10
    letras_erradas = []
    letras_corretas = []

    while True:
    
        for letra in palavra_secreta:
            if letra in letras_corretas:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        print('\n')

        letra = input('Digite uma letra: ').lower()

        if letra in letras_erradas or letra in letras_corretas:
            print('Você já tentou essa letra. Tente novamente.\n')
            continue

        if letra in palavra_secreta:
            letras_corretas.append(letra)
        else:
            letras_erradas.append(letra)
            vidas -= 1

        if vidas == 0:
            print('Você perdeu! A palavra secreta era:', palavra_secreta)
            break

        if all(letra in letras_corretas for letra in palavra_secreta):
            print('Parabéns! Você acertou a palavra secreta:', palavra_secreta)
            break

        print('Letras erradas:', letras_erradas)
        print('Vidas restantes:', vidas)
        print('\n')


jogar_forca()