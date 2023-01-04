print(f'Comanda do pedido\n{("_")*30}\n\nQuantidade | produto   |valor\n\n\n')

print(f'\n {("teste").ljust(10, " ")}{("teste").ljust(10, " ")}{("teste").ljust(10, " ")}')

valor = ( 10.9, 5.40, 8.30, 3.40)
produto = ('Lanche', 'Refri', 'Batata', 'Bombom')
pedido=[]
valorTotal=0
while True:
    try:
        for i in range(len(produto[:])):
            pergunta=input(f'gostaria de {produto[i]} no valor de {valor[i]}?  (S/N)').lower()
            if pergunta == 's':
                quantidade=int(input(f'Quantos {produto[i]} voê deseja?'))
                pedido.append(quantidade)

            else:
                pedido.append(0)
                continue

        print(f'{(" PEDIDO ").center(30,".")}')
        for contador in range(len(produto[:])):
            print(f'{pedido[contador]} {produto[contador]} valor do {contador+1}° pedido foi de R${(pedido[contador]*valor[contador]):.2f}')
            valorTotal+=pedido[contador]*valor[contador]
        print(f'Valor total do pedido foi de R${(valorTotal):.2f}')
        break            
    

       
    except ValueError:
        loop=input('Algo de errado. deseja continuar?  (S/N)').lower()
        if loop=='s':
            continue
        else:
            print('fim do programa!')
            break