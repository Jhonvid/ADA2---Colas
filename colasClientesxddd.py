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


class SistemaColas:
    def __init__(self):
        self.servicios = {
            1: Cola(),  # Cola para servicio 1
            2: Cola(),  # Cola para servicio 2
            3: Cola()   # Cola para servicio 3
        }
        self.numeros_atencion = {
            1: 0,  # Número de atención para servicio 1
            2: 0,  # Número de atención para servicio 2
            3: 0   # Número de atención para servicio 3
        }

    def llegada_cliente(self, servicio):
        if servicio in self.servicios:
            self.numeros_atencion[servicio] += 1
            numero_asignado = self.numeros_atencion[servicio]
            self.servicios[servicio].encolar(numero_asignado)
            print(f"Cliente {numero_asignado} asignado al servicio {servicio}.")
        else:
            print("Servicio no válido.")

    def atender_cliente(self, servicio):
        if servicio in self.servicios:
            if not self.servicios[servicio].esta_vacia():
                cliente_atendido = self.servicios[servicio].desencolar()
                print(f"Atendiendo al cliente {cliente_atendido} del servicio {servicio}.")
            else:
                print(f"No hay clientes en la cola del servicio {servicio}.")
        else:
            print("Servicio no válido.")

    def ejecutar(self):
        while True:
            comando = input("Ingrese un comando (C para llegada, A para atender, S para salir): ").strip().upper()

            if comando == 'S':
                print("Saliendo del sistema.")
                break
            elif comando.startswith('C'):
                try:
                    servicio = int(comando[1:])
                    self.llegada_cliente(servicio)
                except ValueError:
                    print("Formato incorrecto. Use C seguido del número del servicio.")
            elif comando.startswith('A'):
                try:
                    servicio = int(comando[1:])
                    self.atender_cliente(servicio)
                except ValueError:
                    print("Formato incorrecto. Use A seguido del número del servicio.")
            else:
                print("Comando no válido. Intente de nuevo.")


# Ejemplo de uso
sistema = SistemaColas()
sistema.ejecutar()
