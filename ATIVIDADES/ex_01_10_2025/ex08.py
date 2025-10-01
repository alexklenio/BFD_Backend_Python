
def analisar_lista(list):
    result = []
    result.append(sum(list))
    result.append(max(list))

    minha_tupla = tuple(result)
    
    return minha_tupla

print(analisar_lista([9, 2, 25, 55]))