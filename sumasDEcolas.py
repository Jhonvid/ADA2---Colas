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
    paso = 1
    while not cola1.esta_vacia() and not cola2.esta_vacia():
        valor1 = cola1.desencolar()
        valor2 = cola2.desencolar()
        suma = valor1 + valor2
        print(f"\nPaso {paso}:")
        print(f"Desencolando {valor1} de Cola A y {valor2} de Cola B.")
        print(f"Cola A después del desencolado: {cola1}")
        print(f"Cola B después del desencolado: {cola2}")
        print(f"Suma = {suma}")
        cola_resultado.encolar(suma)
        print(f"Cola Resultado tras el paso {paso}: {cola_resultado}")
        paso += 1
    return cola_resultado


colaA = Cola()
colaB = Cola()

for num in [3, 4, 2, 8, 12]:
    colaA.encolar(num)

for num in [6, 2, 9, 11, 3]:
    colaB.encolar(num)

print("Cola A inicial:", colaA)
print("Cola B inicial:", colaB)

cola_resultado = sumar_colas(colaA, colaB)

print("\nCola Resultado final:", cola_resultado)
