vanus=int(input('Sisestage enda vanus: '))
sugu=input('Sisestage enda sugu: ').lower() 
print('treeningu tüübi (1 - tervisetreening, 2 - põhivastupidavuse treening, 3 - intensiivne aeroobne treening)')
style=int(input('Sisestage Treeningutüüp: '))
mMax = 220 - vanus
nMax = 206 - vanus * .88
mminTervis= int(mMax * .5)
mmaxTervis= int(mMax * .7)
mmaxBasic= int(mMax * .8)
mmaxIntensive= int(mMax * .87)

nminTervis= int(nMax * .5)
nmaxTervis= int(nMax * .7)
nmaxBasic= int(nMax * .8)
nmaxIntensive= int(nMax * .87)

if (style==1 and sugu[0:]=='m'):
	print('Pulsisagedus peaks olema vahemikus '+ str(mminTervis)+' kuni '+str(mmaxTervis))
elif (style==2 and sugu[0:]=='m'):
  print('Pulsisagedus peaks olema vahemikus '+ str(mmaxTervis)+' kuni '+str(mmaxBasic))
elif (style==3 and sugu[0:]=='m'):
  print('Pulsisagedus peaks olema vahemikus '+ str(mmaxBasic)+' kuni '+str(mmaxIntensive))

if (style==1 and sugu[0:]=='n'):
	print('Pulsisagedus peaks olema vahemikus '+ str(nminTervis)+' kuni '+str(nmaxTervis))
elif (style==2 and sugu[0:]=='n'):
  print('Pulsisagedus peaks olema vahemikus '+ str(nmaxTervis)+' kuni '+str(nmaxBasic))
elif (style==3 and sugu[0:]=='n'):
  print('Pulsisagedus peaks olema vahemikus '+ str(nmaxBasic)+' kuni '+str(nmaxIntensive))
