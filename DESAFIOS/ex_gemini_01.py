def compras():

    itens = []

    while True:
        item = str(input('\nInforme um item:  '))
        itens.append(item)
        choice = str(input('\nGostaria de adicionar mais itens (S / N)')).upper().strip()

        if choice == "N":
         break
        
    return itens


def lista(itens):
   
   print("-"*20)
   print('Lista de compras')
   print("-"*20)
   
   
   for i, item in enumerate(itens):
      print(f'{i+1} - {item}')
    

def prog():
   lista_de_itens = compras()
   lista(lista_de_itens)


prog()