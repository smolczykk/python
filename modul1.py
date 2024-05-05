def even_numbers(list):
    suma = 0
    for x in list:
        if x % 2 == 0:
            suma += x
    print(suma)
