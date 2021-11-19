import random

def TitSize():
    l=["(",".",")"]
    for size in range(random.randint(0,11)):
        l.insert( 1, ' ')
        n=len(l)
        l.insert( n-1, " ")
    print('your tit size is: ')
    for j in range(2):
        for i in l:
            print(i, end='')

    print()

while True:
    input('press enter to reveal tit size')
    TitSize()