def rebased():
    aasta=int(input('Sisesta aasta: '))
    if (aasta>=2011 and aasta<=2019):
        return True;
    else:
        print('Sisesta aasta 2011-2019')
        return rebased()
rebased()
nr=aasta-2011
fail = open("rebased.txt", encoding="UTF-8")
vastuvõetud = []
for nr, rida in fail:
     vastuvõetud.append(int(rida))
fail.close()
    