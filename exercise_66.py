num = sum_total = count = 0

while True:
    num = int(input('[999 to stop] Type a number: '))
    if num == 999:
        break
    sum_total += num
    count += 1
print(f'\nTotal of numbers: {count}\nSum of numbers: {sum_total}')