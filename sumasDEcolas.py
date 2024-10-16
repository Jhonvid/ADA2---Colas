class Cola:
    def __init__(self):
        self.items = []
    
    def encolar(self, item):
        self.items.append(item)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            raise IndexError("Desencolar desde una cola vacía.")
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def __str__(self):
        return str(self.items)


def sumar_colas(cola1, cola2):
    cola_resultado = Cola()
    while not cola1.esta_vacia() and not cola2.esta_vacia():
        valor1 = cola1.desencolar()
        valor2 = cola2.desencolar()
        cola_resultado.encolar(valor1 + valor2)
    return cola_resultado


colaA = Cola()
colaB = Cola()

for num in [3, 4, 2, 8, 12]:
    colaA.encolar(num)

for num in [6, 2, 9, 11, 3]:
    colaB.encolar(num)

print("Cola A:", colaA)
print("Cola B:", colaB)

cola_resultado = sumar_colas(colaA, colaB)

print("Cola Resultado:", cola_resultado)
