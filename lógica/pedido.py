while True:
    pedido = int(input('Qual o número do seu pedido no cardápio? '))
    
    if pedido == 1:
        print('Big Super | R$5,00')
        break
    
    elif pedido == 2:
        print('Quase Super | R$3,00')
        break
    
    elif pedido == 3:
        print('Mirradus Sanduba | R$1,50')
        break
    
    else:
        print('Temos apenas 3 opções...')