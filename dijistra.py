class Vertice:
    def __init__(self, id) -> None:
        self.id = id
        self.vecinos = list()
        self.visitado = False
        self.padre = None
        self.distance = float("inf")
        
    def agregarVecino(self, v, p):
        if v not in self.vecinos:
            self.vecinos.append([v, p])
            
class Grafica:
    def __init__(self) -> None:
        self.vertices = {}
    
    def agregarVertice(self, id):
        if id not in self.vertices:
            self.vertices[id] = Vertice(id)
            
    def agregarArista(self, a, b, p):
        if a in self.vertices and b in self.vertices:
            self.vertices[a].agregarVecino(b, p)
            self.vertices[b].agregarVecino(a, p)
    
    
    def imprimirGrafica(self):
        for v in self.vertices:
            print("La distancia del vertice " + str(v) + "es "+ str(self.vertices[v].distancia)+ "llegado desde " + str(self.vertices[v].padre))
    
    def camino(self, a , b):
        camino = []
        actual = b
        while actual != None:
            camino.insert(0, actual)
            actual = self.vertices[b].padre
        return[camino, self.vertices[b].distancia]
    
    
    def minimo(self, lista):
        if len(lista) > 0 :
            m = self.vertices[lista[0]].distancia
            v = lista[0] 
            for e in lista:
                if m> self.vertices[e].distancia:
                    m= self.vertices[e].distancia
                    v =e
            return v    
            
    def dijistra(self, a):
        if a in self.vertices:
            self.vertices[a].distancia = 0
            actual = a
            noVisitados = []
            for v in self.vertices:
                if v != a:
                    self.vertices[v].distancia = float("inf")
                self.vertices[v].padre =None
                noVisitados.append(v)
                
            while len(noVisitados) >0:
                for vecino in self.vertices[actual].vecinos:
                    if self.vertices[vecino[0]].visitado == False:
                        if self.vertices[actual].distancia + vecino[1] < self.vertices[vecino[0]].distancia:
                            self.vertices[vecino[0]].distancia = self[actual].distancia + vecino[1]
                            self.vertices[vecino[0]].padre = actual
                self.vertices[actual].visitado = True
                noVisitados.remove(actual)
                
                actual = self.minimo(noVisitados)
        else:
            return False
        
        
class main:
    g =Grafica()
    g.agregarVertice(1)
    g.agregarVertice()