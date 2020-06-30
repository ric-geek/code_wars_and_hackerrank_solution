def high_and_low(numbers):
    
    lista = list(map(int, numbers.split()))

    lista.sort()

    if(len(lista) == 1):
    
        return  str(lista[0]) + " " + str(lista[0])
        
    return str(lista.pop()) + " " + str(lista[0])