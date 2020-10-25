#95562 Diogo Miguel da Silva Santos

#TAD posicao--------------------------------------------------------------------

#Lista 
#Construtor
def cria_posicao(x,y):
    '''
    
cria_posicao: N -> posicao
cria posicao(x,y) recebe os valores correspondentes as coordenadas de uma posicao e devolve a posicao correspondente

    '''
    
    if not isinstance(x,int) or x<0 or not isinstance(y,int) or y<0:
        raise ValueError("cria_posicao: argumentos invalidos")
    
    return [x,y]

def cria_copia_posicao(p):
    '''
    
cria_copia_posicao: posicao -> posicao
cria_copia_posicao(p) recebe uma posicao e devolve um copia da nova posicao

    '''
    
    return cria_posicao(p[0],p[1])

#Seletores
def obter_pos_x(p):
    '''
    
obter_pos_x: posicao -> N    
obter_pos_x(p) devolve a c omponente x da posicao p

    '''
    
    return p[0]

def obter_pos_y(p):
    '''
    
obter_pos_y: posicao -> N
obter_pos_y(p) devolve a componente y da posicao p

    '''
    
    return p[1]

#Reconhecedor
def eh_posicao(arg):
    '''
    
eh_posicao: universal -> booleano
eh_posicao(arg) devolve True caso o seu argumento seja um TAD posicao e False caso contrario

    '''
    
    return isinstance(arg,list) and len(arg)==2 and isinstance(obter_pos_x(arg),int) and obter_pos_x(arg)>=0 and isinstance(obter_pos_y(arg),int) and obter_pos_y(arg)>=0

#Teste    
def posicoes_iguais(p1,p2):
    '''
    
posicoes_iguais: posicao x posicao -> booleano
poicoes_iguais(p1,p2) devolve True apenas se p1 e p2 sao posicoes iguais

    '''
    
    return obter_pos_x(p1)==obter_pos_x(p2) and obter_pos_y(p1)==obter_pos_y(p2)
    
#Transformador    
def posicao_para_str(p):
    '''
    
posicoes_para_str: posicao -> str
posicao_para_str(p) devolve a cadeia de caracteres '(x,y)' que representa o seu argumento, sendo os valores x e y as coordenadas de p

    '''
    
    return str((obter_pos_x(p),obter_pos_y(p)))
    
#Alto Nivel
def obter_posicoes_adjacentes(p):
    '''
    
obter_posicoes_adjacentes: posicao -> tuplo de posicoes
obter_posicoes_adjacentes(p) devolve um tuplo com as posicoes adjacentes a posicao p de acordo com a ordem de leitura de um labirinto

    '''
    
    posicoes_adjacentes=[]
    
    if obter_pos_y(p)-1>0:
        p1=cria_posicao(obter_pos_x(p),obter_pos_y(p)-1)
        posicoes_adjacentes+=[p1]    
    if obter_pos_x(p)-1>0:
        p2=cria_posicao(obter_pos_x(p)-1,obter_pos_y(p))
        posicoes_adjacentes+=[p2]
        
    p3=cria_posicao(obter_pos_x(p)+1,obter_pos_y(p))
    p4=cria_posicao(obter_pos_x(p),obter_pos_y(p)+1)
    
    posicoes_adjacentes+=[p3,p4]
            
    return tuple(posicoes_adjacentes)
   
#TAD unidade--------------------------------------------------------------------

#Lista
#Construtor
def cria_unidade(p,v,f,cad):
    '''
    
cria_unidade: posicao x N x N x str -> unidade
cria_unidade(p,v,f,str) recebe uma posicao p, dois valores inteiros maiores que 0 correspondentes a vida e a forca da unidade, e uma cadeia de caracteres nao vazia correspondente ao exercito da unidade e devolve a unidade correspondente

    '''
    
    if not eh_posicao(p) or not isinstance(v,int) or v<=0 or not isinstance(f,int) or f<=0 or not isinstance(cad,str) or len(cad)==0:
        raise ValueError("cria_unidade: argumentos invalidos")
    
    return [p,v,f,cad]
    
def cria_copia_unidade(u):
    '''
    
cria_copia_unidade: unidade -> unidade
cria_copia_unidade(u) recebe uma unidade u e devolve uma nova copia da undiade

    '''
    
    copia_unidade=[]
    p,v,f,cad=u[0],u[1],u[2],u[3]
    copia_unidade=[p,v,f,cad]
    
    return copia_unidade

#Seletores
def obter_posicao(u):
    '''
    
obter_posicao: unidade -> posicao
obter_posicao(u) devolve a posicao da unidade u 

    '''
    
    return u[0]

def obter_exercito(u):
    '''
    
obter_exercito: unidade -> str
obter_exercito(u) devolve a cadeia de carateres correspondente ao exercito da unidade

    '''
    
    return u[3]

def obter_forca(u):
    '''
    
obter_forca: unidade -> N
obter_forca(u) devolve o valor corresponde a forca de ataque da unidade

    '''
    
    return u[2]

def obter_vida(u):
    '''
    
obter_vida: unidade -> N
obter_vida(u) devolve o valor corresponde aos pontos de vida da unidade

    '''
    
    return u[1]

def muda_posicao(u,p):
    '''
    
muda_posicao: unidade x posicao -> unidade
muda_posicao(u,p) modifica destrutivamente a unidade u alterando a usa posicao com o novo valor p, e devolve a propria unidade

    '''
    
    u[0]=p
    
    return u

def remove_vida(u,v):
    '''
    
remove_vida: unidade x N -> unidade
remove_vida(u,v) modifica destrutivamente a unidade u alterando os seus pontos de vida subtraindo o valor v, e devolve a propria unidade

    '''
    
    u[1]-=v
    
    return u

#Reconhecedor
def eh_unidade(arg):
    '''
    
eh_unidade: universal -> booleano
eh_unidade(arg) devolve True caso o seu argumento seja um TAD unidade e False caso contrario

    '''
    
    return isinstance(arg,list) and len(arg)==4 and eh_posicao(obter_posicao(arg)) and isinstance(obter_vida(arg),int) and obter_vida(arg)>0 and isinstance(obter_forca(arg),int) and obter_forca(arg)>0 and isinstance(obter_exercito(arg),str)

#Teste
def unidades_iguais(u1,u2):
    '''
    
unidades_iguais: unidade x unidade -> booleano
unidades_iguais(u1, u2) devolve True apenas se u1 e u2 sao unidades iguais

    '''
    
    return obter_posicao(u1)==obter_posicao(u2) and obter_vida(u1)==obter_vida(u2) and obter_forca(u1)==obter_forca(u2) and obter_exercito(u1)==obter_exercito(u2)

#Transformadores
def unidade_para_char(u):
    '''
    
unidade_para_char: unidade -> str
unidade_para_char(u) devolve a cadeia de caracteres dum unico elemento, correspondente ao primeiro caracter em maiuscula do exercito da unidade passada por argumento

    '''
    
    return obter_exercito(u)[0].upper()


def unidade_para_str(u):
    '''
    
unidade_para_str: unidade -> str
unidade_para_str(u) devolve a cadeia de caracteres que representa a unidade como mostrado nos exemplos a seguir

    '''
    
    return (unidade_para_char(u)+str([obter_vida(u),obter_forca(u)])+'@'+str((obter_posicao(u)[0],obter_posicao(u)[1])))

#Alto Nivel
def unidade_ataca(u1,u2):
    '''
    
unidade_ataca: unidade x unidade -> booleano
unidade_ataca(u1,u2) modifica destrutivamente a unidade u2 retirando o valor de pontos de vida correspondente a forca de ataque da unidade u1. A funcao devolve True se a undiade u2 for destruida ou False caso contrario

    '''
    
    remove_vida(u2,obter_forca(u1))
    
    return obter_vida(u2)<=0


def  ordenar_unidades(t):
    '''
    
ordenar_unidades: tuplo unidades -> tuplo unidades
ordenar_unidades(t) devolve um tuplo contendo as mesmas unidades do tuplo fornecido como argumento, ordenadas de acordo com a ordem de leitura do labirinto

    '''
    
    posicoes=[]
    ordenada=[]
    
    for unidade in t:
        posicoes+=[obter_posicao(unidade)]
        
    posicoes=sorted(posicoes, key=lambda k: [obter_pos_y(k),obter_pos_x(k)])   #ordena a posicoes primeiro pelos valores de y e depois pelos valores de x
    
    for posicao in posicoes:
        for unidade in t:
            if posicao in unidade:
                ordenada+=[unidade]  #recria o tuplo com as unidades ordenadas a partir das posicoes ja ordenadas
                
    return tuple(ordenada)
        
    
#TAD mapa-----------------------------------------------------------------------

#Dicionario
#Construtor
def cria_mapa(d,w,e1,e2):
    '''
    
cria_mapa: tuplo x tuplo x tuplo x tuplo -> mapa
cria_mapa(d, w, e1, e2) recebe um tuplo d de 2 valores inteiros correspondentes as dimensoes Nx e Ny do labirinto,um tuplo w de 0 ou mais posicoes correspondentes as paredes que nao sao dos limites exteriores do labirinto, um tuplo e1 de 1 ou mais unidades do mesmo exercito, e um tuplo e2 de um ou mais unidades de um outro exercito e devolve o mapa que representa internamente o labirinto e as unidades presentes

    '''
    
    if not isinstance(d,tuple) or len(d)!=2 or not isinstance(d[0],int) or not isinstance(d[1],int) or (d[0] or d[1])<=2 or not isinstance(w,tuple) or not isinstance(e1,tuple) or len(e1)<1 or not isinstance(e2,tuple) or len(e2)<1:
        raise ValueError("cria_mapa: argumentos invalidos")
    
    for posicao in w:             #Verifica se a posicoes de w estao nas paredes
        if not eh_posicao(posicao):
            raise ValueError("cria_mapa: argumentos invalidos")
        elif posicao[0] in [0,d[0]] and (posicao[1] ==0 or posicao[1]==d[1]) :
            raise ValueError("cria_mapa: argumentos invalidos")
        elif posicao[1] in [0,d[1]] and (posicao[0]==0 or posicao[0]==d[0]):
            raise ValueError("cria_mapa: argumentos invalidos")
        elif posicao[0]>=d[0] or posicao[1]>=d[1]:
            raise ValueError("cria_mapa: argumentos invalidos")
        
    for unidade in e1:   #Verifica se os elementos de cada exercito sao unidades
        if not eh_unidade(unidade):
            raise ValueError("cria_mapa: argumentos invalidos")
    for unidade in e2:
        if not eh_unidade(unidade):
            raise ValueError("cria_mapa:argumentos invalidos")
        
    return {"dim":d,"paredes":w,"exercito1":e1,"exercito2":e2}

def cria_copia_mapa(m):
    '''
    
cria_copia_mapa: mapa -> mapa
cria_copia_mapa(m) recebe um mapa e devolve uma nova copia do mapa

    '''
    
    novo_mapa={} 
    
    d=m["dim"]
    w=m["paredes"]
    
    e1=[]
    for unidade in m["exercito1"]:
        e1+=[cria_copia_unidade(unidade)]
        
    e2=[]
    for unidade in m["exercito2"]:
        e2+=[cria_copia_unidade(unidade)]
        
    novo_mapa={"dim":d,"paredes":w,"exercito1":tuple(e1),"exercito2":tuple(e2)}
    
    return novo_mapa

#Seletores
def obter_tamanho(m):
    '''
    
obter_tamanho: mapa -> tuplo
obter_tamanho(m) devolve um tuplo de dois valores inteiros correspondendo o primeiro deles a dimensao Nx e o segundo a dimensao Ny do mapa

    '''
    
    return (m["dim"][0],m["dim"][1])

def obter_nome_exercitos(m):
    '''
    
obter_nome_exercitos: mapa -> tuplo 
obter_nome_exercitos(m) devolve um tuplo ordenado com duas cadeias de caracteres correspondendo aos nomes dos exercitos do mapa    

    '''
    
    if len(m["exercito1"])>0 and len(m["exercito2"])>0:    #Verifica se o exercito contem unidades
        nomes=[m["exercito1"][0][3],m["exercito2"][0][3]]
    else:
        if len(m["exercito1"])>0:  
            nomes=m["exercito1"][0][3]
        elif len(m["exercito2"])>0:
            nomes=m["exercito2"][0][3]
        
    return tuple(sorted(nomes))

def obter_unidades_exercito(m,e):
    '''
    
obter_unidades_exercito: mapa x str -> tuplo unidades
obter_unidades_exercito(m, e) devolve um tuplo contendo as unidades do mapa pertencentes ao exercito indicado pela cadeia de caracteres e, ordenadas em ordem de leitura do labirinto

    '''
    
    unidades=[]
    
    if len(m["exercito1"])>0:            #Verifica se o exercito contem unidades
        if e == m["exercito1"][0][3]:
            for unidade in m["exercito1"]:
                unidades+=[unidade]
    if len(m["exercito2"])>0:
        if e==m["exercito2"][0][3]:
            for unidade in m["exercito2"]:
                unidades+=[unidade]
            
    return ordenar_unidades(unidades)

def obter_todas_unidades(m):
    '''
    
obter_todas_unidades: mapa -> tuplo
obter_todas_unidades(m) devolve um tuplo contendo todas as unidades do mapa, ordenadas em ordem de leitura do labirinto

    '''
    
    exercito1=()
    exercito2=()
    
    if len(m["exercito1"])>0:            #Verifica se o exercito contem unidades
        exercito1=obter_unidades_exercito(m,m["exercito1"][0][3])
    if len(m["exercito2"])>0:
        exercito2=obter_unidades_exercito(m,m["exercito2"][0][3])
        
    return ordenar_unidades(exercito1+exercito2)
    
def obter_unidade(m,p):
    '''
    
obter_unidade: mapa x posicao -> unidade
obter_unidade(m, p) devolve a unidade do mapa que se encontra na posicao p

    '''
    
    for unidade in m["exercito1"]:         #Percorre todas as unidades ate obter aquela que tem como posicao 'p'
        if p==obter_posicao(unidade):  
            return unidade      
        
    for unidade in m["exercito2"]:
        if p==obter_posicao(unidade):
            return unidade

#Modificadores
def eliminar_unidade(m,u):
    '''
    
eliminar_unidade: mapa x unidade -> mapa
eliminar_unidade(m,u) modifica destrutivamente o mapa m eliminando a unidade u do mapa e deixando livre a posicao onde se encontrava a undiade. Devolve o proprio mapa

    '''
    
    if u in m["exercito1"]:
        novo=list(m["exercito1"])
        novo.remove(u)
        m["exercito1"]=novo
        
    elif u in m["exercito2"]:
        novo=list(m["exercito2"])
        novo.remove(u)
        m["exercito2"]=novo
        
    return m
    
def mover_unidade(m,u,p):
    '''
    
mover_unidade: mapa x unidade x poicao -> mapa
mover_unidade(m,u,p) modifica destrutivamente o mapa m e unidade u alterando a posicao da unidade no mapa para a nova posicao p e deixando livre a posicao onde se encontrava. Devolve o proprio mapa

    '''
    
    muda_posicao(u,p)
    
    return m

def eh_posicao_unidade(m,p):
    '''
    
eh_posicao_unidade: mapa x posicao -> booleano
eh_posicao_unidade(m, p) devolve True apenas no caso da posicao p do mapa estar ocupada por uma unidade

    '''
    
    for unidade in obter_todas_unidades(m):
        if [obter_pos_x(p),obter_pos_y(p)]==obter_posicao(unidade):
            return True
        
    return False
         
def eh_posicao_corredor(m,p):
    '''
    
eh_posicao_corredor: mapa x posicao -> booleano
eh_posicao_corredor(m, p) devolve True apenas no caso da posicao p do mapa corresponder a um corredor no labirinto (independentemente de estar ou nao ocupado por uma unidade)

    '''
    
    posicao=[obter_pos_x(p),obter_pos_y(p)]
    
    return not eh_posicao_parede(m,posicao) and posicao not in m["paredes"]

def eh_posicao_parede(m,p):
    '''
    
eh_posicao_parede: mapa x posicao -> booleano
eh_posicao_parede(m, p) devolve True apenas no caso da posicao p do mapa corresponder a uma parede do labirinto

    '''
    
    coord_x_max=obter_tamanho(m)[0]-1 #Nx 
    coord_y_max=obter_tamanho(m)[1]-1 #Ny
    
    if (p[1]==0 or p[1]==coord_y_max) and p[0] in range(0,coord_x_max+1):
        return True
    elif (p[0]==0 or p[0]==coord_x_max) and p[1] in range(0,coord_y_max+1): 
        return True
    elif list(p) in m["paredes"]:
        return True
    else:
        return False
    
#Teste
def mapas_iguais(m1,m2):
    '''
    
mapas_iguais: mapa x mapa -> booleano
mapas_iguais(m1, m2) devolve True apenas se m1 e m2 forem mapas iguais

    '''
    
    return m1["dim"]==m2["dim"] and m1["paredes"]==m2["paredes"] and m1["exercito1"]==m2["exercito1"] and m1["exercito2"]==m2["exercito2"]

#Transformador
def mapa_para_str(u):
    '''
    
mapa_para_str: mapa -> str
mapa_para_str(u) devolve uma cadeia de caracteres que representa o mapa como descrito no primeiro projeto, neste caso, com as unidades representadas pela sua representacao externa

    '''
    
    mapa=''
    
#Percorre todas as posicoes de uma linha antes de passar para a linha de baixo
    for y in range(obter_tamanho(u)[1]):   
        for x in range(obter_tamanho(u)[0]):    #Percorre cada x dentro da mesma linha                
            if eh_posicao_unidade(u,cria_posicao(x,y)):
                mapa+=unidade_para_char(obter_unidade(u,cria_posicao(x,y)))  
            elif eh_posicao_parede(u,cria_posicao(x,y)):
                mapa+='#'
            elif eh_posicao_corredor(u,cria_posicao(x,y)):
                mapa+='.'
            else:
                mapa+='#' #se nao for nem um corredor nem uma parede entao e um limite exterior
        mapa+='\n'
        
    return mapa[:-1]

#Alto Nivel
def obter_inimigos_adjacentes(m,u):
    '''
    
obter_inimigos_adjacentes: mapa x unidade -> tuplo unidades
obter_inimigos_adjacentes(m, u) devolve um tuplo contendo as unidades inimigas adjacentes a unidade u de acordo com a ordem de leitura do labirinto

    '''
    
    exercitos=obter_nome_exercitos(m)
    exercito1,exercito2=obter_unidades_exercito(m,exercitos[0]),obter_unidades_exercito(m,exercitos[1])
    unidades_inimigas=[]
    
    if u in exercito1:                                              #Decide a qual dos exercitos pertence u
        for posicao in obter_posicoes_adjacentes(obter_posicao(u)): #percorre as posicoes adjacentes de u
            if obter_unidade(m,posicao) in exercito2:               #e aquelas que forem inimigas sao adicionadas a lista de inimigos adjacentes 
                unidades_inimigas+=[obter_unidade(m,posicao)]
    else:
        for posicao in obter_posicoes_adjacentes(obter_posicao(u)):
            if obter_unidade(m,posicao) in exercito1:
                unidades_inimigas+=[obter_unidade(m,posicao)]   
                
    return ordenar_unidades(unidades_inimigas)
                
def obter_movimento(mapa, unit):
    '''
    A funcao obter_movimento devolve a posicao seguinte da unidade argumento
    de acordo com as regras de movimento das unidades no labirinto.

    obter_movimento: mapa x unidade -> posicao
    '''

    ######################
    # Funcoes auxiliares #
    ######################
    def pos_to_tuple(pos):
        return obter_pos_x(pos), obter_pos_y(pos)

    def tuple_to_pos(tup):
        return cria_posicao(tup[0], tup[1])

    def tira_repetidos(tup_posicoes):
        conj_tuplos = set(tuple(map(pos_to_tuple, tup_posicoes)))
        return tuple(map(tuple_to_pos, conj_tuplos))

    def obter_objetivos(source):
        enemy_side = tuple(filter(lambda u: u != obter_exercito(source), obter_nome_exercitos(mapa)))[0]
        target_units = obter_unidades_exercito(mapa, enemy_side)
        tup_com_repetidos = \
            tuple(adj
                  for other_unit in target_units
                  for adj in obter_posicoes_adjacentes(obter_posicao(other_unit))
                  if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj))
        return tira_repetidos(tup_com_repetidos)

    def backtrack(target):
        result = ()
        while target is not None:
            result = (target,) + result
            target, _ = visited[target]
        return result

    ####################
    # Funcao principal #
    ####################
    # Nao mexer se ja esta' adjacente a inimigo
    if obter_inimigos_adjacentes(mapa, unit):
        return obter_posicao(unit)

    visited = {}
    # posicao a explorar, posicao anterior e distancia
    to_explore = [(pos_to_tuple(obter_posicao(unit)), None, 0)]
    # registro do numero de passos minimo ate primeira posicao objetivo
    min_dist = None
    # estrutura que guarda todas as posicoes objetivo a igual minima distancia
    min_dist_targets = []

    targets = tuple(pos_to_tuple(obj) for obj in obter_objetivos(unit))

    while to_explore:  # enquanto nao esteja vazio
        pos, previous, dist = to_explore.pop(0)

        if pos not in visited:  # posicao foi ja explorada?
            visited[pos] = (previous, dist)  # registro no conjunto de exploracao
            if pos in targets:  # se a posicao atual eh uma dos objetivos
                # se eh primeiro objetivo  ou se esta a  distancia minima
                if min_dist is None or dist == min_dist:
                    # acrescentor 'a lista de posicoes minimas
                    min_dist = dist
                    min_dist_targets.append(pos)
            else:  # nao 'e objetivo, acrescento adjacentes
                for adj in obter_posicoes_adjacentes(tuple_to_pos(pos)):
                    if eh_posicao_corredor(mapa, adj) and not eh_posicao_unidade(mapa, adj):
                        to_explore.append((pos_to_tuple(adj), pos, dist + 1))

        # Parar se estou a visitar posicoes mais distantes que o minimo,
        # ou se ja encontrei todos os objetivos
        if (min_dist is not None and dist > min_dist) or len(min_dist_targets) == len(targets):
            break

    # se encontrei pelo menos uma posicao objetivo, 
    # escolhe a de ordem de leitura menor e devolve o primeiro movimento
    if len(min_dist_targets) > 0:
        # primeiro dos objetivos em ordem de leitura
        tar = sorted(min_dist_targets, key=lambda x: (x[1], x[0]))[0]
        path = backtrack(tar)
        return tuple_to_pos(path[1]) 

    # Caso nenhuma posicao seja alcancavel
    return obter_posicao(unit)
 
 
#Funcoes adicionais----------------------------------------------------------------------------
 
def calcula_pontos(m,e):
    '''
    
calcula_pontos: mapa x str -> int
Funcao auxiliar que recebe um mapa e uma cadeia de caracteres correspondente ao nome de um dos exercitos do mapa e devolve a sua pontuacao. A pontuacao dum exercito e o total dos pontos de vida de todas as unidades do exercito

    '''
    
    pontuacao=0
    
    if len(obter_unidades_exercito(m,e))==0: #Caso o exercito esteja vazio devolve 0
        return pontuacao
    if e==obter_nome_exercitos(m)[0]:
        for unidade in obter_unidades_exercito(m,e):    
            pontuacao+=obter_vida(unidade)            #soma os varios pontos de vida de todas as unidades de um exercito
    else: #e==obter_nome_exercitos(m)[1]:
        for unidade in obter_unidades_exercito(m,e):
            pontuacao+=obter_vida(unidade)
            
    return pontuacao

def simula_turno(m):
    '''
    
simula_turno: mapa -> mapa
Funcao auxiliar que modifica o mapa fornecido como argumento de acordo com a simulacao de um turno de batalha completo, e devovle o proprio mapa. Iste e,seguindo a ordem de leitura do labirinto, cada unidade(viva) realiza um unico movimento e um ataque de acordo com as regras descritas

    '''          
    
    unidades=obter_todas_unidades(m)
    
#Cria um ciclo que atualiza todas as posicoes ( atualiza-> mover/atacar )
    while len(unidades)>0:    
        mover_unidade(m,unidades[0],obter_movimento(m,unidades[0]))             #a unidade movimenta se
        if len(obter_inimigos_adjacentes(m,unidades[0]))>=1:                    #se tiver inimigos nas suas posicoes adjacentes ataca
            if unidade_ataca(unidades[0],obter_inimigos_adjacentes(m,unidades[0])[0])==True:  #se a vida do inimigo adjacente for menor ou igual a zero vai ser removido das unidades
                inimigo=obter_inimigos_adjacentes(m,unidades[0])[0]
                eliminar_unidade(m,obter_inimigos_adjacentes(m,unidades[0])[0])  
                if inimigo in unidades:      
#Verifica se o inimigo que vamos retirar da lista ainda esta na lista para evitar o erro de remover uma unidade que ja teve o seu turno (e que por isso nao esta na lista "unidades")
                    lista_unidades=list(unidades)            
                    lista_unidades.remove(inimigo)          
                    unidades=tuple(lista_unidades)
        unidades=unidades[1:]  #passa para a proxima unidade
        
    return m
        
def simula_batalha(cad,b):
    '''
    
simula_batalha: str x booleano -> str
Funcao principal que permite simular uma batalha completa, recebe uma cadeia de caracteres e um valor booleano e devolve o nome do exercito ganhador.Em caso de empate, a funcao deve devolver a cadeia de caracteres 'EMPATE'.
A cadeia de caracteres passada por argumento corresponde ao ficheiro de configuracao do simulador. O argumento booleano ativa o movo verboso(True) ou o modo quiet(False). No modo quiet mostra se pela saida standard o mapa e a pontuacao no inicio da simulacao e apos do ultimo turno de batalha. No modo verboso, mostra se tambem o mapa e a pontuacao apos de cada turno de batalha.

    '''
    
    nome_ficheiro=cad
    ficheiro=open(nome_ficheiro,'r')
    
    #LER FICHEIROS
    d=eval(ficheiro.readline())
    u1_dados=eval(ficheiro.readline())  #nome,vida,forca
    u2_dados=eval(ficheiro.readline())
    w_posicoes=eval(ficheiro.readline())
    u1_posicoes=eval(ficheiro.readline())
    u2_posicoes=eval(ficheiro.readline())
    
    ficheiro.close()
    
    #CRIAR EXERCITOS
    exercito1=tuple(cria_unidade(cria_copia_posicao(posicao),u1_dados[1],u1_dados[2],u1_dados[0]) for posicao in u1_posicoes)
    exercito2=tuple(cria_unidade(cria_copia_posicao(posicao),u2_dados[1],u2_dados[2],u2_dados[0]) for posicao in u2_posicoes)
    
    #CRIAR PAREDES
    paredes=tuple(cria_copia_posicao(posicao) for posicao in w_posicoes)
    
    #CRIAR MAPA
    mapa=cria_mapa(d,paredes,tuple(exercito1),tuple(exercito2))
    
    exercito1_nome=obter_nome_exercitos(mapa)[0]
    exercito2_nome=obter_nome_exercitos(mapa)[1]
    
    #MAPAS E PONTUACAO
    mapa_inicial=mapa_para_str(mapa)
    pontuacao=("[ "+exercito1_nome+":"+str(calcula_pontos(mapa,exercito1_nome))+" "+exercito2_nome+":"+str(calcula_pontos(mapa,exercito2_nome))+" ]")
   
    
    #Inicializacao
    print(mapa_inicial)
    print(pontuacao)
    
    #Verboso
    if b==True:
        
        while 0!=1:     #ciclo que permite a iteracao dos varios turnos ate que chegue ao fim da batalha
            
            if calcula_pontos(mapa,exercito1_nome)==0 and calcula_pontos(mapa,exercito2_nome)==0:
                return 'EMPATE'
            elif calcula_pontos(mapa,exercito1_nome)==0:
                return exercito2_nome
            elif calcula_pontos(mapa,exercito2_nome)==0:
                return exercito1_nome
                    
            #Atualiza as variaveis e mostra o novo mapa/pontuacao  
            
            mapa_antigo=cria_copia_mapa(mapa)
            simula_turno(mapa)
            mapa_novo=cria_copia_mapa(mapa)
            
            print(mapa_para_str(mapa))
            print(("[ "+exercito1_nome+":"+str(calcula_pontos(mapa,exercito1_nome))+" "+exercito2_nome+":"+str(calcula_pontos(mapa,exercito2_nome))+" ]"))
            
            if mapas_iguais(mapa_antigo,mapa_novo):
                return 'EMPATE'
    
    #Quiet
    elif b==False:  #a diferenca de b=True para b=False e que apenas da print quando a batalha acabar
        
        while 0!=1:
            
            if calcula_pontos(mapa,exercito1_nome)==0 and calcula_pontos(mapa,exercito2_nome)==0:
                print(mapa_para_str(simula_turno(mapa)))
                print(("[ "+exercito1_nome+":"+str(calcula_pontos(mapa,exercito1_nome))+" "+exercito2_nome+":"+str(calcula_pontos(mapa,exercito2_nome))+" ]") )                
                return 'EMPATE'
            
            elif calcula_pontos(mapa,exercito1_nome)==0:
                print(mapa_para_str(simula_turno(mapa)))
                print(("[ "+exercito1_nome+":"+str(calcula_pontos(mapa,exercito1_nome))+" "+exercito2_nome+":"+str(calcula_pontos(mapa,exercito2_nome))+" ]") )                
                return exercito2_nome
            
            elif calcula_pontos(mapa,exercito2_nome)==0:
                print(mapa_para_str(simula_turno(mapa)))
                print(("[ "+exercito1_nome+":"+str(calcula_pontos(mapa,exercito1_nome))+" "+exercito2_nome+":"+str(calcula_pontos(mapa,exercito2_nome))+" ]") )                
                return exercito1_nome
            
             #Atualiza as variaveis
                    
            mapa_antigo=cria_copia_mapa(mapa)
            simula_turno(mapa)
            mapa_novo=cria_copia_mapa(mapa)
            
            if mapas_iguais(mapa_antigo,mapa_novo):
                print(mapa_para_str(simula_turno(mapa)))
                print(("[ "+exercito1_nome+":"+str(calcula_pontos(mapa,exercito1_nome))+" "+exercito2_nome+":"+str(calcula_pontos(mapa,exercito2_nome))+" ]") )                    
                return 'EMPATE'               