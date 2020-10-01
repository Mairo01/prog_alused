kp = str(input('Sisesta kujul DD.MM.YYYY: '))
def kuu_nimi():
    kuud=['Jaanuar','Veebruar','Marts','Aprill','Mai','Juuni','Juuli','august','september','oktoober','november','detsember']
    l=kp.split(".")
    kuuNR=int(l[1])
    kuu = kuud[kuuNR-1]
    print(l[0] +". " + kuu + " " + l[2])
kuu_nimi()
