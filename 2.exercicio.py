cardapio = [['Lanche', 10.9], ['Batata',  5.5], ['Refri' ,  3.9]]
produtos=[] 
comanda=[]
valor=0

pergunta=input('Deseja algo? ')[0].lower()
if pergunta in 's':
    print(f'{("Cardapio").center(25," ")}\nProduto {("Valor").rjust(18," ")}')

    for contador in cardapio:
        print(f'{contador[0].ljust(20,".")} R$ {contador[1]:.2f}')

    for i in cardapio:
        produtos.append(i[0])
                
    print(produtos)
    
    while True:
        pedido=input('Segue o cardapio, Oque deseja?  ').capitalize()
        if pedido not in produtos:

            pedido=input(f'O item {pedido} não esta no cardapio. Deseja algo mais?  (S/N)').lower()
            if pedido == 's':
                continue

            else:
                if comanda == []:
                    print('Não houve pedido.')

                else:
                    
                    print(f'\n{("Itens escolhidos").center(37," ")}\n')
                    for i in comanda:
    
                        print(f'{i[2]}: {i[0].ljust(21, ".")} valor  R$ {(i[2]*i[1]):.2f}')
                        valor+=i[2]*i[1]
                    print(f'\nO valor total do pedido foi de  R$ {valor:.2f}')
                    break
                    
        else:
            quantidadePedido=int(input(f'Quantos {pedido} você quer? '))
            comanda.append([pedido],[cardapio[produtos.index(pedido)][1]],[quantidadePedido])
            cardapio.append(comanda[:])


            print(comanda)

            loop=input('Algo mais? (S/N)').lower()
            if loop == 's':
                continue
            else:
                if comanda == []:
                    print('Não houve pedido.')

                else:
                    
                    print(f'\n{("Itens escolhidos").center(37," ")}\n')
                    for i in comanda:
    
                        print(f'{i[2]}: {i[0].ljust(21, ".")} valor  R$ {(i[2]*i[1]):.2f}')
                        valor+=i[2]*i[1]
                    print(f'\nO valor total do pedido foi de  R$ {valor:.2f}')
                    break
                
else:
    print('Não foi realizado pedido.\nAté a proxima.')