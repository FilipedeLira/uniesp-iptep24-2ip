# função de processamento do progama
def funcao_processamento():


    dragao1 = float(input('digite o tempo do dragao 1:'))
    dragao2 = float(input('digite o tempo do dragao 2:'))

    DISTANCIA = 1000


    vel_dga1 = DISTANCIA/dragao1
    vel_dga2 = DISTANCIA/dragao2

    if  vel_dga1 > vel_dga2:
        print('o Banguela (1) é o mias veloz')
    elif vel_dga2 > vel_dga1:
        print('O Banguela não é o mais veloz')
    else:
        print('Os dois dragões tem a mesma velocidade!')

if  __name__ == '__main__':
    # mensagem de inicio de progama
    print('--- --- iniciando progama --- ---')
    
    # processamento realizado pelo progama
    funcao_processamento()

    # mensagem de fim do progama
    print('--- --- fim do progama --- ---')


