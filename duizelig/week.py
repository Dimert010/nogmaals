welkedag = input('geef een dag van de week: ')
alledagen = ['maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag']
maakIndex = alledagen.index(welkedag)
sliceIndex = alledagen[:maakIndex+1]
while welkedag in alledagen:
    print(*sliceIndex)
    break