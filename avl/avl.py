# Implementa un Arbol AVL

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1

# Arbol AVL
class AVL:
    # Inserta un nodo en el arbol
    def insertar(self, raiz, valor):
        if not raiz:
            return Nodo(valor)
        elif valor < raiz.valor:
            raiz.izq = self.insertar(raiz.izq, valor)
        else:
            raiz.der = self.insertar(raiz.der, valor)
    
        raiz.altura = 1 + max(self.altura(raiz.izq), self.altura(raiz.der))
    
        balance = self.getBalance(raiz)
    
        # Caso 1: izquierda izquierda
        if balance > 1 and valor < raiz.izq.valor:
            return self.rotacionDerecha(raiz)
    
        # Caso 2: derecha derecha
        if balance < -1 and valor > raiz.der.valor:
            return self.rotacionIzquierda(raiz)
    
        # Caso 3: izquierda derecha
        if balance > 1 and valor > raiz.izq.valor:
            raiz.izq = self.rotacionIzquierda(raiz.izq)
            return self.rotacionDerecha(raiz)
    
        # Caso 4: derecha izquierda
        if balance < -1 and valor < raiz.der.valor:
            raiz.der = self.rotacionDerecha(raiz.der)
            return self.rotacionIzquierda(raiz)
    
        return raiz
    
    # Elimina un nodo del arbol
    def eliminar(self, raiz, valor):
        if not raiz:
            return raiz
    
        elif valor < raiz.valor:
            raiz.izq = self.eliminar(raiz.izq, valor)
    
        elif valor > raiz.valor:
            raiz.der = self.eliminar(raiz.der, valor)
    
        else:
            if raiz.izq is None:
                temp = raiz.der
                raiz = None
                return temp
    
            elif raiz.der is None:
                temp = raiz.izq
                raiz = None
                return temp
    
            temp = self.valorMinimoNodo(raiz.der)
            raiz.valor = temp.valor
            raiz.der = self.eliminar(raiz.der, temp.valor)
    
        if raiz is None:
            return raiz
        
        raiz.altura = 1 + max(self.altura(raiz.izq), self.altura(raiz.der))
         
        balance = self.getBalance(raiz)
        
    
        # Caso 1: izquierda izquierda
        if balance > 1 and self.getBalance(raiz.izq) >= 0:
            return self.rotacionDerecha(raiz)
         
        # Caso 2: izquierda derecha
        if balance > 1 and self.getBalance(raiz.izq) < 0:
            raiz.izq = self.rotacionIzquierda(raiz.izq)
            return self.rotacionDerecha(raiz)
        
        # Caso 3: derecha derecha
        if balance < -1 and self.getBalance(raiz.der) <= 0:
            return self.rotacionIzquierda(raiz)
        
        # Caso 4: derecha izquierda
        if balance < -1 and self.getBalance(raiz.der) > 0:
            raiz.der = self.rotacionDerecha(raiz.der)
            return self.rotacionIzquierda(raiz)
         
        return raiz
    
    # Busca un nodo en el arbol
    def buscar(self, raiz, valor):
        if not raiz:
            return False
        elif raiz.valor == valor:
            return True
        elif valor < raiz.valor:
            return self.buscar(raiz.izq, valor)
        else:
            return self.buscar(raiz.der, valor)
    
    # Obtiene el valor minimo de un nodo
    def valorMinimoNodo(self, nodo):
        current = nodo
    
        while(current.izq is not None):
            current = current.izq
    
        return current
    
    # Obtiene la altura de un nodo
    def altura(self, nodo):
        if not nodo:
            return 0
    
        return nodo.altura
     
    # Obtiene el balance de un nodo
    def getBalance(self, nodo):
        if not nodo:
            return 0
    
        return self.altura(nodo.izq) - self.altura(nodo.der)
     
    # Rotacion a la derecha
    def rotacionDerecha(self, z):
        y = z.izq
        T2 = y.der
    
        y.der = z
        z.izq = T2
    
        z.altura = 1 + max(self.altura(z.izq), self.altura(z.der))
        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))
    
        return y
     
    # Rotacion a la izquierda
    def rotacionIzquierda(self, z):
        y = z.der
        T2 = y.izq
    
        y.izq = z
        z.der = T2
    
        z.altura = 1 + max(self.altura(z.izq), self.altura(z.der))
        y.altura = 1 + max(self.altura(y.izq), self.altura(y.der))
    
        return y
     
    # Imprime el arbol
    def imprimir(self, raiz):
        if raiz:
            self.imprimir(raiz.izq)
            print(raiz.valor)
            self.imprimir(raiz.der)

if __name__ == '__main__':
     
    # Crea el arbol de prueba
    arbol = AVL()
    raiz = None
    
    raiz = arbol.insertar(raiz, 10)
    
    arbol.imprimir(raiz)
    
    arbol.insertar(raiz, 20)
    
    arbol.imprimir(raiz)
    
    arbol.insertar(raiz, 30)
    
    arbol.imprimir(raiz)
    
    arbol.insertar(raiz, 40)
    
    arbol.imprimir(raiz)
    
    