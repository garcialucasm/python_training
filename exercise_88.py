import random
temp = i = 0
bet = []
bets = []

print('-'*40)
a_num = int(input('How many times do you want to bet? '))
print('-'*40)

for c in range(0,a_num):
    while True:
        temp = random.randint(1, 60)
        if temp not in bet:
            bet.append(temp)
            i += 1
        if i >= 6:
            break
    bet.sort()
    bets.append(bet[:])
    print(f'{c+1}º Bet : {bets[c]}')
    bet.clear()
    i = 0

print('-'*40)
print('GOOD LUCK!')
print('-'*40)