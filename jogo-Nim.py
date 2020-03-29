
def inicializacao():
    global maquina
    cont = 1
    pc = 0
    jogador = 0

    print("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada")
    escolha = int(input("2 - para jogar um campeonato "))
    if escolha == 2:
        print("Voce escolheu um campeonato!")
        
        while cont < 4:
            print("**** Rodada ",cont,"****")
            partida()
            if maquina:
                pc += 1
                print('Fim do jogo! O computador ganhou!')
                
            else:
                jogador += 1
                print('Fim do jogo! Você ganhou!')
            
            cont += 1
            continue

        print('**** Final do campeonato! ****')
        print('Placar: Você ',jogador,' X ',pc,' Computador')
    else:
        print("Voce escolheu uma partida isolada")
        partida()
        if maquina:
            print('Fim do jogo! O computador ganhou!')
            
        else:
            print('Fim do jogo! Você ganhou!')

def computador_escolhe_jogada(n, m):
    global z
    if n>0 and m>0 and n>m:
        if m > 1:
            q = n // (m + 1)
            z =  n - (q*(m+1))
    
            while z == 0:
                z = (m-1)
        else:
            z = 1
    else:
        m = n
        z = n
        
    return z


def usuario_escolhe_jogada(n, m):
    global z
    if m > n:
        m = n
    if n > 0 and m > 0 and n >= m:
        z = int(input("Quantas peças voce vai retirar? "))
        while z > m or z <= 0:
            z = int(input("Quantas peças voce vai retirar? "))
            continue
    return z

def partida():
    global z
    global inicio
    global usuario
    global maquina

    inicio = 0
    usuario = 0
    maquina = 0

    n = int(input('Quantas peças? '))
    m = int(input('Limites de peças por jogada? '))
   
    while m>n or n<=0 or m<=0:
        n = int(input('Quantas peças? '))
        m = int(input('Limites de peças por jogada? '))
        continue
    
    while n > 0 and not inicio:
    
        if m > 1:

            if n%(m+1) == 0:
                print("Você começa!")
                inicio = 1
                usuario = 1
                maquina = 0
                usuario_escolhe_jogada(n, m)
                n = n - z
                print('Você tirou',str(z),' peças.')
                print('Agora restam',str(n),' peças no tabuleiro.')    

            else:
                print("Computador começa!")
                inicio = 1
                usuario = 0
                maquina = 1
                computador_escolhe_jogada(n, m)
                n = n - z
                print('O computador tirou',str(z),'peças.')
                print('Agora restam',str(n),' peças no tabuleiro.')

        else:
            if n % 2 == 0:
                print("Você começa!")
                inicio = 1
                usuario = 1
                maquina = 0
                usuario_escolhe_jogada(n, m)
                n = n - z
                print('Você tirou',str(z),' peças.')
                print('Agora restam',str(n),' peças no tabuleiro.')    
            else:
                print("Computador começa!")
                inicio = 1
                usuario = 0
                maquina = 1
                computador_escolhe_jogada(n, m)
                n = n - z
                print('O computador tirou',str(z),'peças.')
                print('Agora restam',str(n),' peças no tabuleiro.')
       
       
       
    while n > 0 and inicio:
            
        trans = 0

        if usuario and not maquina and not trans:
            maquina = 1
            usuario = 0
            computador_escolhe_jogada(n, m)
            n = n - z
            print('O computador tirou',str(z),'peças.')
            print('Agora restam',str(n),' peças no tabuleiro.')
            trans = 1
        else:
            if not trans:
                maquina = 0
                usuario = 1
                usuario_escolhe_jogada(n, m)
                n = n - z
                print('Você tirou',str(z),' peças.')
                print('Agora restam',str(n),' peças no tabuleiro.')    
                trans = 1                          
        continue

    return maquina 

inicializacao()
