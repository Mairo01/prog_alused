nimi = input('Sisesta Leedu perekonnanimi: ')
if nimi[-2:]=='ne':
	print('Abielus')
elif nimi[-2:]=='te':
	print('vallaline')
elif nimi[-1:]=='e':
	print('Maaramata')
else:
	print('Pole ilmselt leedulanna')