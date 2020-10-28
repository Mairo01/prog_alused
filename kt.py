import random
Kmin=60
Kmax=600
koned=[]
kmHind=float(input("Sisesta kõneminuti hind: "))
koguarv=int(input("Sisesta kõnede koguarv: "))
i=0
def kone_maksumus():
  ksumma=round(kmHind*konekestvus/60, 2)
  print(ksumma)
  return True
  
while i<koguarv:
  konekestvus=random.randint(1, 1000)
  koned.append(konekestvus)
  kone_maksumus()
  summa=kmHind*konekestvus/60
  p= round(summa+summa, 2)
  i += 1
print("Maksumus kokku " + str(p))