def player_data(p_player='<unknown>', p_goals=0):
    print(f'The player {p_player} scored {p_goals} goals.')


a_player = str(input('Enter the name of the player: '))
a_goals = str(input(f'How many goals did {a_player} make? '))
if a_goals.isnumeric():
    a_goals = int(a_goals)
else:
    a_goals = 0
if a_player.strip() == '':
    player_data(p_goals=a_goals)
else:
    player_data(a_player, a_goals)
