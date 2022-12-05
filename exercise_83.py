# validation of math expressions

pilha = []

while True:

    expression = str(input('Enter the expression:'))
    for simb in expression:
        if simb == '(':
            pilha.append('(')
        elif simb == ')':
            if len(pilha) > 0:
                pilha.pop()
            else:
                pilha.append(')')
                break
    if len(pilha) == 0:
        print('Expression OK')
    else:
        print('Expression NOK')
    print(len(pilha))


    op = ' '
    while not op in 'YN':
        op = str(input('Do you want to try another expression? [Y/N] ')).upper()
    if op == 'N':
        break
    else:
        pass
