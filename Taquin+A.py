import random
import time
import os
matriz=[]
listayausados=[]
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)


def CrearTablero(x,listayausados,matriz):
  
  yaprimera=False
  if listayausados:
    yaprimera=True
  tam=int(x)
  
  lista=[]
  
  for i in range (0,tam):
    
    contador=1
    
    flag=True
    numerocandi=0
    
      
    if contador<=tam*tam:        
      while flag:          
        if listayausados and yaprimera :            
          numerocandi=random.randint(1,tam*tam ) 
          if numerocandi in listayausados:
            flag=True
          else:              
            flag=False                          
              
          #if flag and contador>1:
          #    print('entra 2222')
          #    listayausados.append(numerocandi)
          #    lista.append(numerocandi)  
                 
        else:
          yaprimera=True
          flag=False
          print('hola')
          
          numerocandi=random.randint(1,tam*tam )            
          listayausados.append(numerocandi)
          
          
            
            
            
    if flag==False :
      if len(listayausados)>=1:
       listayausados.append(numerocandi)
       lista.append(numerocandi)          
      
       contador+=1
    
    

  matriz.append(lista)  
  
  
   
   
def imprimirmatriz(matriz):
  for i in range (0,len(matriz)):
   print(matriz[i])



  

    
  
  
if __name__ == "__main__":
  while True:
   clearConsole()
   try: 
    print("=============Bienvenidos a Takin===============")
    Tamano=input('Digite el tamano del tablero\n')
    aux=int(Tamano)
    break
   except ValueError and aux>0:
     print("Por favor introdusca un valor numerico no negativo")
     time.sleep(1.53)
  print("Creandoooo Tablero")
  
  #s=nodo(matriz,matriz,0)
     
  for i in range (0,aux):
    
   CrearTablero(Tamano,listayausados,matriz)
  
  for k in range (0, len(matriz)):
   for j in range (0,len(matriz[i])):
    if matriz[k][j]==aux*aux:
     matriz[k][j]='X'
      
  imprimirmatriz(matriz)
'''
Algoritmo de Juego automatico usando busqueda a*
class nodo:
  def __init__(self, TAQUIN, padre=None, accion=None):
        self.padre = padre
        self.TAQUIN = TAQUIN       
        self.accion = accion
        if (self.padre != None):
            self.giro = padre.g + 1
        else:
            self.giro = 0

    @property
    def puntaje(self):
        return (self.giro + self.hilo)

    @property
    def estado(self):
        
        return str(self)

    @property 
    def caminoe(self):
        
        nodoaux
        d = self, []
        while node:
            d.append(node)
            nodoaux = node.padre
        yield from cambio(d)

    @property
    def solucionado(self):
        
        return self.TAQUIN.solucionado

    @property
    def accion(self):
        
        return self.TAQUIN.accion

    @property
    def hilo(self):
        
        return self.TAQUIN.manhattan

    @property
    def suma(self):
       
        return self.hilo + self.giro

    def to_string(self):
        return str(self.TAQUIN)


class TAQUIN:
   
    def __init__(self, tablero):
        self.ancho = len(tablero[0])
        self.tablero = tablero

  
        

    @property 
    def movimientos(self):
       
       
       
        for i, j in TABLERO.producto(range(self.ancho),
                                      range(self.ancho)):
            tiposmovimiento = {'AB':(i, j-1),
                      'A':(i, j+1),
                      'I':(i-1, j),
                      'D':(i+1, j)}

            for accion, (r, c) in direcs.items():
                if r >= 0  and r < self.ancho and 
                self.ancho>0: 
                   self.tablero[r][c] == 0:
                    mover = crear_movimiento((i,j), (r,c)), 
                    
                    moverf.append(mover)
        return mover

    @property
    def DManhatan(self,n):
        crear_movimiento = 0
        for i in range(n):
            for j in range(n):
                if self.tablero[i][j] != 'x':
                    x, y = divmod(self.board[i][j]-1, 4)
                    crear_movimiento += abs(x - i) + abs(y -j)
        return crear_movimiento

    

    def copiar_tablero(self):
        
        tablero = []
        for row in self.tablero:
            tablero.append([x for x in row])
        return Taquin(tablero)

    def mover(self, inicio, fin):
       
        copia = self.copiar_tablero()
        i, j = at
        r, c = to
        copiar_tablero.tablero[i][j], copiar_tablero.tablero[r][c] = 
          copiar_tablero.tablero[r][c], copiar_tablero.tablero[i][j]
        return copia

    def pprint(self):
        for r in self.board:
            print(r)
      

    

class Soluciona:
   
    def __init__(self, inicio):
        self.inicio = inicio

    def soluciona(self):
      
        cola = collections.deque([Node(self.inicio)])
        recorrido = set()
        recorrido.add(cola[0].state)
        while cola:
            
            nodo = cola.popleft()
            if nodo.solved:
                return nodo.path

           
            else 
               return ('no existe Solucion ')
'''