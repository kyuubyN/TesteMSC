import random
import emoji
import math
import playsound

n7 = float(input('Selecione um numero: '))
n6 = math.sqrt(n7)
print(emoji.emojize('A raiz desse numero é {:.0f} :star: '.format(n6), use_aliases=True))

n1 = input('Primeiro participante: ')
n2 = input('Segundo participante: ')
n3 = input('Terceiro participante: ')
n4 = ([n1, n1, n3])
n5 = random.choice(n4)
print(emoji.emojize(f'O ganhador é {n5} :smile: +999999999 Social points', use_aliases=True))

playsound.playsound('Musica3.mp3')


