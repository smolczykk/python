def srednia_liczb(lista):
    suma_liczb = 0
    for x in lista:
        suma_liczb += x
    length = len(lista)
    wynik = suma_liczb / length
    print(wynik)


