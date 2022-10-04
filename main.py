import random
'''
this code is in portuguese
below will be some translations for better understanding of the code

Pedra = Rock
Papel = Paper
Tesoura = Scissor

Empate = Draw
Vitória = Win
Derrota = Defeat

'''
op = ['Pedra', 'Papel', 'Tesoura']
y = random.choice(op)

while True:


    x = input('Pedra, Papel ou Tesoura: ')


    if x == 'Pedra':
        if y == 'Pedra':
            print('{} vs {} = Empate' .format(x, y))
        elif y == 'Tesoura':
            print('{} vs {} = Vitória' .format(x,y))
        elif y == 'Papel':
            print('{} vs {} = Derrota' .format(x,y))
    elif x == 'Papel':
        if y == 'Papel':
            print('{} vs {} = Empate'.format(x, y))
        if y == 'Pedra':
            print('{} vs {} = Vitória'.format(x, y))
        elif y == 'Tesoura':
            print('{} vs {} = Derrota'.format(x, y))
    elif x == 'Tesoura':
        if y == 'Tesoura':
            print('{} vs {} = Empate'.format(x, y))
        elif y == 'Papel':
            print('{} vs {} = Vitória'.format(x, y))
        elif y == 'Pedra':
            print('{} vs {} = Derrota'.format(x, y))

    a = input('Quer jogar de novo s/n')
    if a == 's':
        y = random.choice(op)
        continue
    elif a == 'n':
        break

print('Obrigado por jogar!')




