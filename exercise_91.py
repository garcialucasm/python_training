from random import randint
game = list()
player = dict()
ranking = list()
for c in range(1, 5):
    player['player'] = c
    player['score'] = randint(1, 6)
    game.append(player.copy())
print('-='*20)
print(f'RANDOM GAME')
print('-='*20)
for i in game:
    for k, v in i.items():
        print(f'{k} {v} ',end='')
    print()
print('-'*40)
ranking = sorted(game, key=lambda x:x['score'], reverse=True)
for i, v in enumerate(ranking):
    print(f"{i+1}º --> Player {v['player']} | Score {v['score']}")






