Nimi = str(input("Sisestage oma nimi: "))
LubatudKiirus = int(input('Sisestage suurim lubatud kiirus: '))
Kiirus = int(input('Sisestage tegelik kiirus: '))
Trahv = int(3*(Kiirus - LubatudKiirus))
if Trahv <= 0:
    print(Nimi + 'ei saanud trahvi')
elif Trahv >= 190:
    print(Nimi + ' sai trahvi 190 eurot ')
else:
    print(Nimi + ' sai trahvi ' + str(Trahv))

#trahv= min(190, (Kiirus-LubatudKiirus)*3 )



