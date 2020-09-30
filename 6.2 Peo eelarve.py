kutsutud=int(input('Kutsutud '))
tuleb=int(input('Tuleb '))
def eelarve(kutsutud, tuleb):
    max=kutsutud*10+55
    min=tuleb*10+55
    print('Maksimaalne eelarve: ' + str(max) + ' eurot')
    print('Minimaalne eelarve: ' + str(min) + ' eurot')
eelarve(kutsutud, tuleb)