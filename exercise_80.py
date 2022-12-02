a_list = []

for c in range (0,5):
    number = int(input('Enter a number: '))

    if number in a_list:
        while True:
            print('This value already exists in the list.')
            number = int(input('Enter a number: '))
            if number not in a_list:
                break
    if c == 0 or number > a_list[-1]:
        a_list.append(number)
        print(f'Number {number} added at index {a_list.index(number)}')
    else:
        for i in range(len(a_list)):
            if number <= a_list[i]:
                a_list.insert(i, number)
                print(f'Number {number} added at index {a_list.index(number)}')
                break
print(30*'-=')
print(f'Sorted values: {a_list}')
 




