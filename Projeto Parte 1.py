#95562  Diogo Miguel da Silva Santos

#-------------------------------------------FUNCOES---------------------------------------------
                                          
#2.1.1
def eh_labirinto (maze):  
#Verifica se o maze e um tuplo
    if not isinstance(maze,tuple):
        return False
#Verifica se o maze tem o numero minimo de tuplos    
    if len(maze)<3:
        return False
    for tuplo in range(len(maze)):
#Verifica se os elementos do maze sao tuplos
        if not isinstance(maze[tuplo],tuple):
            return False
#Verifica se os elementos do maze tem o numero minimo de numeros
        if  len(maze[tuplo])<3:
            return False
#Verifica se os elementos do maze tem todos o mesmo tamanho
        else:
            n=len(maze[0])
            for elem in maze: 
                if n != len(elem):
                    return False        
        for i in range(len(maze[tuplo])):
#Verifica se os elementos do maze sao inteiros e se sao exclusivamente 0 ou 1
            if (type(maze[tuplo][i]) is int) ==False:
                return False
            elif maze[tuplo][i] not in [0,1]:
                return False         
#Verifica se as posicoes externas correspondem sempre a paredes
    for i in range(len(maze)):                
        if (maze[i][0] and maze[i][-1]) != 1:
            return False
        else:
            for elem in maze[i]:
                if (maze[0][elem] or maze[-1][elem]) != 1:
                    return False  
    return True

#2.1.2
def eh_posicao (posicao): 
    if not isinstance(posicao,tuple):
        return False
#Verifica se a posicao tem tamanho correto
    if len(posicao) != 2:    
        return False
#Verifica se os valores sao inteiros e positivos
    for i in range(0,2):                    
        if not isinstance(posicao[i],int) or posicao[i]<0:
            return False
    return True
        

#2.1.3
def eh_conj_posicoes (conj):
#Verifica se o conjunto e tuplo se os seus elementos sao tuplos e se os valores dos elementos sao inteiros e positivos
    if not isinstance(conj,tuple):
        return False
    for elem in range(len(conj)):
        if (type(conj[elem]) is tuple)==False:
            return False
        if eh_posicao(conj[elem]) == False:
            return False
        for n in range(len(conj[elem])):
            if (type(conj[elem][n]) is int)==False or conj[elem][n]<0:
                return False    
#Verifica se existem elementos repetidos no conjunto
        conj_sem_repetidos=()
        for elem in range(len(conj)):
            if conj[elem] not in conj_sem_repetidos:
                conj_sem_repetidos+=(conj[elem],)
        if conj_sem_repetidos != conj:
            return False
    return True

#2.1.4
def tamanho_labirinto (maze):
#Verifica se o maze dado e um labirinto
    if not eh_labirinto(maze):
        raise ValueError("tamanho_labirinto: argumento invalido")
    
    else:
        Nx=len(maze)
        Ny=len(maze[0])
        return (Nx,)+(Ny,)


#2.1.5
def eh_mapa_valido(maze,conj):
#Verifica os argumentos
    if not(eh_labirinto(maze)==True and eh_conj_posicoes(conj)==True):
        raise ValueError("eh_mapa_valido: algum dos argumentos e invalido")
    
#Verifica se os elementos do conjunto sao validos atraves de uma funcao auxiliar
    for elem in conj:
        if posicao_pertence(maze,elem)==False:
            return False
    return True
    
#Funcao Auxiliar (1): Verificar se uma posicao pertence ao labirinto
#Utilizada diretamente em 2.1.5 e em 2.1.6
def posicao_pertence(maze,posicao):
    if eh_posicao(posicao)==False:
        return False
    coord_max_x=tamanho_labirinto(maze)[0]-1
    coord_max_y=tamanho_labirinto(maze)[1]-1
    if posicao[0] >= coord_max_x or posicao[1] >= coord_max_y:
        return False
#Verifica se a posicao comeca ou acaba com zero ( Nesse caso estaria numa parede )
    if posicao[0]==0 or posicao[1]==0:
        return False 
#Verifica se a posicao corresponde a uma parede do labirinto
    x=posicao[0]
    y=posicao[1]
    if maze[x][y]==1:
        return False
    return True

#2.1.6
def eh_posicao_livre(maze,conj,posicao):
#Verifica argumentos
    if not(eh_labirinto(maze)==True and eh_posicao(posicao)==True and eh_conj_posicoes(conj)==True and eh_mapa_valido(maze,conj)==True):
        raise ValueError("eh_posicao_livre: algum dos argumentos e invalido") 
    
#Verifica se a posicao pertence ao maze e que nao esta em nenhuma parede
    if not posicao_pertence(maze,posicao):
        return False
#Verifica se a posicao esta a ocupar uma unidade do conjunto
    for elem in range(len(conj)):
        if conj[elem] == posicao:
            return False
    return True

#2.1.7
def posicoes_adjacentes(posicao):
#Verifica argumentos
    if not eh_posicao(posicao):
        raise ValueError("posicoes_adjacentes: argumento invalido")
    
#Cria os tuplos adjacente
    tuplo_cima=((posicao)[0],(posicao)[1]-1)
    tuplo_esquerda=((posicao)[0]-1,(posicao)[1])
    tuplo_direita=((posicao[0]+1,(posicao)[1]))
    tuplo_baixo=((posicao)[0],(posicao)[1]+1)
    lista_tuplos=[tuplo_cima,tuplo_esquerda,tuplo_direita,tuplo_baixo]
    conj_tuplos_adjacentes=()
#Verifica se os tuplos adjacentes sao validos
    for tuplo in lista_tuplos:
        if tuplo[0] >= 0 and tuplo[1] >= 0:
            conj_tuplos_adjacentes+= (tuplo,)
    return conj_tuplos_adjacentes
    
#2.1.8
def mapa_str (maze,conj):
#Verifica argumentos
    if not(eh_labirinto(maze)==True and eh_conj_posicoes(conj)==True):
        raise ValueError("mapa_str: algum dos argumentos e invalido")
    if not eh_mapa_valido(maze,conj):
        raise ValueError("mapa_str: algum dos argumentos e invalido")
    
    n=0   #Utilizado para fazer o ciclo while passar por todos os tuplos do labirinto
    mapa=[]  #Mapa em formato "lista" para depois poder alterar
#Pegar no primeiro elemento de cada tuplo e soma-los numa lista
#Depois passamos para o segundo elemento de cada tuplo e continuamos assim ate ao ultimo tuplo
    while n < len(maze[0]):
        for tuplo in range(len(maze)):
            if maze[tuplo][n] == 1:
                mapa += ['#']
            else:
                mapa += ['.']
        if conj != ():
#Substituir uma posicao do labirinto pelas unidades do conjunto
# conj[x][1] * (len(maze)+1)  leva-nos ate a linha correta do labirinto  (+1 devido ao \n)
# conj[x][0] leva-nos ate a posicao correta dentro dessa linha
            if n == conj[0][0]:
                mapa[conj[0][1]*(len(maze)+1)+conj[0][0]]='O'
            if n == conj[1][0]:
                mapa[conj[1][1]*(len(maze)+1)+conj[1][0]]='O'                
        mapa+='\n'
        n+=1
#Transformamos a lista numa string
    mapa=mapa[:-1]
    return ''.join(mapa)

#2.2.1
def obter_objetivos(maze,conj,posicao):
    if not (eh_labirinto(maze)==True and eh_posicao(posicao)==True and eh_conj_posicoes(conj)==True and eh_mapa_valido(maze,conj)==True and (posicao in conj)==True):
        raise ValueError("obter_objetivos: algum dos argumentos e invalido")
    
    objetivo_adjacentes=()
    objetivo_posicoes=()   #conjunto de todas as posicoes objetivos
#Cria um tuplo com as posicoes adjacentes das unidades que nao sao a posicao
    for elem in conj:
#Verifica se a posicao ja esta no objetivo
        #if posicao in posicoes_adjacentes(elem):
            #return objetivo_posicoes
        if elem != posicao:
            objetivo_adjacentes = objetivo_adjacentes + posicoes_adjacentes(elem)
#Cria um tuplo com as posicoes adjacentes que nao sao paredes
    for elem in objetivo_adjacentes:
        if eh_posicao_livre(maze,conj,elem) and elem not in objetivo_posicoes:
            objetivo_posicoes+=(elem,)
    return objetivo_posicoes


#2.2.2
def obter_caminho(maze,conj,posicao):
    if not (eh_labirinto(maze)==True and eh_posicao(posicao)==True and eh_conj_posicoes(conj)==True and eh_mapa_valido(maze,conj)==True and (posicao in conj)==True):
        raise ValueError("obter_caminho: algum dos argumentos e invalido")
    
    lista_exploracao=[(posicao,())]
    
    objetivos=obter_objetivos(maze,conj,posicao)
    posicoes_visitadas=[]
#Verifica se a posicao ja se encontra no objetivo   
    for elem in conj:
        if posicao in posicoes_adjacentes(elem):
            return ()
#Algoritmo 1 dado no Projeto    
    while lista_exploracao != []:
        posicao_atual=lista_exploracao[0][0]
        caminho_atual=lista_exploracao[0][1]
#Se a posicao ja foi visitada, apaga se
        if posicao_atual in posicoes_visitadas:
            del lista_exploracao[0]
#Caso contrario passa a posicao visitada, o caminho 'cresce'
        if posicao_atual not in posicoes_visitadas:
            posicoes_visitadas+=[posicao_atual]
            if posicao_pertence(maze,posicao_atual):
                caminho_atual+=(posicao_atual,)
#Se a posicao atual ja esta em um do objetivos, devolvemos o caminho que fizemos ate la
            if posicao_atual in objetivos:
                return caminho_atual
            else:
                adjacentes=posicoes_adjacentes(posicao_atual)
#Vamos explorar as posicoes adjacente da posicao atual e voltamos ao while repetindo o projeto para cada uma delas
                for elem in adjacentes:
                    if eh_posicao_livre(maze,conj,elem):
                        lista_exploracao += [(elem,(caminho_atual)),]
    return ()
                        
        
#2.2.3
maze=((1,1,1,1,1,1),(1,0,0,0,0,1),(1,0,0,0,0,1),(1,0,0,0,0,1),(1,1,1,1,1,1),(1,0,0,0,0,1),(1,1,1,1,1,1))
unidades=((2,2),(5,4))

def mover_unidade(maze,conj,posicao):
    if not (eh_labirinto(maze)==True and eh_posicao(posicao)==True and eh_conj_posicoes(conj)==True and eh_mapa_valido(maze,conj)==True and (posicao in conj)==True):
        raise ValueError("mover_unidade: algum dos argumentos e invalido")
    
    conj_atualizado=()
    
    adjacentes=posicoes_adjacentes(posicao)
    objetivos=obter_caminho(maze,conj,posicao)
    
#Se a posicao nao tiver posicoes adjacentes (ex:rodeada de paredes)    
    if len(adjacentes)==0:
        return conj
    if len(objetivos)==0:
        return conj
    for elem in conj:
#Se o elemento nao for a posicao, copia se o valor igual
        if elem!=posicao:
            conj_atualizado+=(elem,)
#Se o elemento for a posicao, atualiza se para a proxima posicao dada pelo obter_caminho
        else:
            conj_atualizado+=(objetivos[1],)
#Se o elemento ja estiver no objetivo, nao faz nada
        if elem in adjacentes:
            return conj
    return conj_atualizado