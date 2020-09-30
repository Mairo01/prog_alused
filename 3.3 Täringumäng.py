import random
k=int(input('Täringute arv: '))
n=0
nr=0
while n<k:
    nr=random.randint(1,6)
    print(nr)
    n+=2