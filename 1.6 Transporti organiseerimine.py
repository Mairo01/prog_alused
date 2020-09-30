busse=int(input('Mitu bussi? '))
istekohad=busse*20
inimesi=int(input('Kui palju inimesi? '))
istekohata=(max(0, inimesi-istekohad))
if istekohata>0:
  print(str(istekohata) + ' inimest jäi istekohata')
else: print('Keegi ei jäänud istekohata')