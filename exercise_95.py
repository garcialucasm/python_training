a_data = dict()
team = list()
matches = list()
goals = sum_goals = 0
a_num = 0

while True:
    a_data.clear()
    matches.clear()
    a_data['name'] = str(input('Enter the name: '))
    a_num = int(input(f"Enter how many matches {a_data['name']} played? "))
    for c in range(0, a_num):
        goals = int(input(f"    Enter how many goals {a_data['name']} scored: "))
        matches.append(goals)
        sum_goals += goals
    a_data['goals'] = matches.copy()
    a_data['total'] = sum_goals
    team.append(a_data.copy())
    op = ' '
    while not op in 'YN':
        op = str(input('Do you want to continue? [Y/N] ')).upper()
    if op == 'N':
        break
    elif op == 'Y':
        pass
print('-' * 30)
print(team)
print('-' * 30)
for k, v in a_data.items():
    print(f'{k:^10}', end="")
print()
print('-' * 30)
for c in team:
    for k, v in c.items():
        print(f'{str(v):^10}', end="")
    print()
print()
print('-' * 30)


