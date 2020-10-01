kuud=['Jaanuar','Veebruar','Marts','Aprill','Mai','Juuni','Juuli','august','september','oktoober','november','detsember']
kp=str(input('Sisesta kujul DD.MM.YYYY: '))
l= kp.split(".")
kuuNR=int(l[1])
kuu = kuud[kuuNR]
print(l[0] +". " + kuu + " " + l[2])
