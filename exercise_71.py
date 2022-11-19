withdraw = int()
total_notes = int()
ced = int(50)
rest = int()

print('-'*30)
print('ATM - BANK ABC')
print('-'*30)


withdraw = int(input('Type a value to withdraw: '))
rest = withdraw

while True:
    if rest >= ced:
        total_notes = rest // ced
        rest = rest % ced
        print(f'Banknotes of {ced}: {total_notes}')
        if rest == 0:
            break
    else:
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1


