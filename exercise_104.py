def readint(p_num):
    checknum = str(input(p_num))
    if checknum.isnumeric():
        pass
    else:
        while True:
            print('ERROR! You have to enter a number!')
            checknum = str(input('Please, enter a number: '))
            if checknum.isnumeric():
                checknum = int(checknum)
                break
    return checknum


a_num = readint('Enter a number: ')
print(f'You just typed the number {a_num}.')