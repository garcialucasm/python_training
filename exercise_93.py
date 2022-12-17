a_data = dict()
matches = list()
goals = sum_goals = 0
a_num = 0

a_data['name'] = str(input('Enter the name: '))
a_num = int(input(f"Enter how many matches {a_data['name']} played? "))
for c in range (0, a_num):
    goals = int(input(f"    Enter how many goals {a_data['name']} scored: "))
    matches.append(goals)
    sum_goals += goals
a_data['goals'] = matches
a_data['total'] = sum_goals
print('-'*30)
print(a_data)
print('-'*30)
for k, v in a_data.items():
    print(f'The key {k} has the value: {v}')
print('-'*30)
print(f"The player {a_data['name']} had {a_num} matches.")
for i, v in enumerate(matches):
    print(f"    Match {i}: {v} goals")
print(f"Total of goals: {a_data['total']}")