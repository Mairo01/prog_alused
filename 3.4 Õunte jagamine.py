k=int(input('Mitu pöialpoissi thab õunu? '))
n=0
nr=0
palju=0
while n<k:
    nr=random.randint(1,2)
    print(nr)
    palju+=nr
    n+=1
print('Lumivalgekesele jäi ' + str(max(0, 14-palju)))