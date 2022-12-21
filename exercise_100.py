from random import randint
from time import sleep


# random from list without repetition
# def n_drawn(p_list):
#     n_random = random.sample(a_list, k=5)
#     print(n_random)


def n_drawn():
    for c in range (0, 5):
        n = randint(0, 10)
        while True:
            if n not in a_list:
                a_list.append(n)
                break
            else:
                n = randint(0, 10)
    print(f'Sorting 5 different values:', end=' ')
    for i in a_list:
        print(i, end=' ')
        sleep(0.5)
    print()


def sum_even():
    even_s = 0
    for i in a_list:
        if i % 2 == 0:
            even_s += i
    print(f'Adding the even values of the list {a_list} we get {even_s}')


a_list = list()
n_drawn()
sum_even()

