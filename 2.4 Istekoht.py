import random
p=random.randint(1, 100)
vIstekoht=input('Kas soovite isekohta ise valida ("ise") või loosida ("loos")? ')
if (vIstekoht == 'loos' and p>100/3):
    print('Istekohaks vahekaik')
elif (vIstekoht == 'loos' and p<100/3):
    print('Istekohaks aknakoht')

if (vIstekoht == 'ise'):
    ivIstekoht=input('Kas soovite istuda akna ääres ("aken") voi mitte ("muu")? ')
elif (vIstekoht == 'ise' and ivIstekoht == 'aken'):
    print('Valisite aknakoha')
elif (vIstekoht == 'ise' and ivIstekoht == 'muu'):
    print('Valisite vahekaigukoha')
