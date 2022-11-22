a_list = []
c = 0
max_index = []
min_index = []

for c in range(0, 4):
    value = int(input(f'Enter the {c+1}º value : '))
    a_list.append(value)
print('-'*30)
max_value = max(a_list)
for i_max in range(len(a_list)):
    if a_list[i_max] == max_value:
        max_index.append(i_max)

min_value = min(a_list)
for i_min in range(len(a_list)):
    if a_list[i_min] == min_value:
        min_index.append(i_min)


print(f'Biggest: {max(a_list)} | Index: {max_index}')
print(f'Biggest: {min(a_list)} | Index: {min_index}')
