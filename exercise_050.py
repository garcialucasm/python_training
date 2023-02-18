num_sum = 0
a_list_sum = list()
for c in range(1,7):
    num_x = 0
    num_x = int(input('Enter the {}º even number : '.format(c)))
    if num_x % 2 == 0:
        num_sum += num_x
        a_list_sum.append(num_x)
    else:
        print('Odd values will not be considered.')
print('Value of the sum of even numbers: {}'.format(num_sum))
