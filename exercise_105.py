def score(*n, sit=False):
    r = dict()
    r['total'] = len(n)
    r['greater'] = max(n)
    r['smaller'] = min(n)
    r['average'] = sum(n)/len(n)
    if sit == True:
        if r['average'] < 6:
            r['situation'] = 'FAIL'
        if 6 <= r['average'] < 8:
            r['situation'] = 'REGULAR'
        if 8 <= r['average'] < 9:
            r['situation'] = 'GOOD'
        if r['average'] >= 9:
            r['situation'] = 'EXCELLENT'

    return r
    print(p_answer)


answer = score(5.5, 2.5, 10, 6.5, sit=True)
print(answer)