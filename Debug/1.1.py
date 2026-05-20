numero_secreto = 7
tentativas = 0

print("Tente adivinhar o número secreto!")

while tentativas < 3:
    chute = int(input("Digite um número: ")) # o bug estava no tipo da variavel, que estava entrando como str em vez de int

    if chute == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    else:
        print("Número errado!")

    tentativas = tentativas + 1

if tentativas == 3:
    print("Fim de jogo!")