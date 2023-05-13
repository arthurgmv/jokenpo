from random import randint
intens = ("Pedra", "Papel", "Tesoura")
computador = randint (0,2)
print ("=+=+"*9)
print ("Jokenpo - Pedra, Papel e Tesoura")
print ("=+=+"*9)

print (''' Suas Opções são:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input("Escolha a sua jogada! "))
if jogador == 0 and computador == 2:
    print ("Você jogou {} e o cumputador jogou {}, parabéns você venceu!".format(intens[jogador],intens[computador]))
elif jogador == 0 and computador == 1:
    print ("Você jogou {} e o computador {}, que pena, você perdeu".format(intens[jogador],intens[computador]))
elif jogador == 1 and computador == 0:
    print ("Você jogou {} e o computador jogou {}, parabéns você vence!".format(intens[jogador],intens[computador]))
elif jogador == 1 and computador == 2:
    print ("Você jogou {} e o computador jogou {}, que pena, você perdeu".format(intens[jogador],intens[computador]))
elif jogador == 2 and computador == 1:
    print ("Você jogou {} e o cumputador jogou {}, parabéns você venceu!".format(intens[jogador],intens[computador]))
elif jogador == 2 and computador == 0: 
    print ("Você jogou {} e o cumputador jogou {}, parabéns você venceu!".format(intens[jogador],intens[computador]))
print ("=+=+"*8)