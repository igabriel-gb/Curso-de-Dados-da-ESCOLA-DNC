cardapio_precos = ('Doce', 2.3, 'Bala', 0.15, 'Pizza', 28.9, 'Arroz', 4.5, 'Paçoca', 0.5, 'Pamonha', 5.4)

cardapio_bar = ('Cerveja', 10.3, 'Porcao', 30.15, 'Pizza', 28.9, 'Refri', 8.5, 'Paçoca', 0.5, 'Peixe', 25.4,'Sinuca', 1.0)

def loja(lista):
    
    cardapio_precos = lista

    def cardapio(lista):
        cardapio_precos = lista
        print(f'\n {"-"*32} \n {("Cardápio").center(32,"-")}\n {"-"*32}')

        for i in range(1,  len(cardapio_precos),2):
            print(f' {cardapio_precos[i-1]} {cardapio_precos[i]}')
        print('_'*50)

    cardapio(cardapio_precos)    

    valor_pedido=0

    comanda=[]

    while True:
        pedido = input('\nOque deseja?:  ').capitalize()

        def itens(comanda,valor_pedido):
            print('_'*50,' \n','Os itens escolhidos foram:\n')
                
            for i in range(len(comanda)):
                print(f'{comanda[i]}')
            print(f'\nTotal: {valor_pedido:.2f}\n')

        if pedido not in cardapio_precos:
            loop = input('O intem não está o menu. Deseja continuar?(S/n): ').lower()
            if loop == 's':
                cardapio(cardapio_precos)
                continue
            else:
                if comanda == []:
                    print('Não Houve pedidos')
                else:
                    itens(comanda,valor_pedido)
                break
        else:
            comanda.append(pedido)
            valor_pedido+=(cardapio_precos[cardapio_precos.index(pedido)+1])
            
            itens(comanda,valor_pedido)

            lool_finalizar_pedido = input(f'Deseja Algo mais?(S/n): ').lower()

            if lool_finalizar_pedido == 's':
                cardapio(cardapio_precos)
                
                continue
            else:
                itens(comanda,valor_pedido)
                break


loja(cardapio_bar)