kSuurus=float(input('Sisestage kirja suurus: '))
kPealkiri=input('Sisestage kirja pealkiri: ')
def Fail():
  kFail=input('Kas kirjaga on fail kaasas? ').lower()
  if (kFail == 'jah' or kFail == 'ei'):
    return True;
  else: 
    print('Jah või Ei')
    return Fail();
Fail()
if (kSuurus<1 and kPealkiri!='' and kFail=='jah'):
  print('Kiri ei ole spämm')
else:
  print('Kiri on tõenäoliselt spämm')