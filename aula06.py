from time import sleep

def enviar_lembrete():
    
    spam = 0
    while spam < 5:
        print(f'Altere sua senha.Lembrete n {spam}')
        spam = spam + 1
         # spam += 1
        sleep(2)

if __name__ == '__main__':
    enviar_lembrete()