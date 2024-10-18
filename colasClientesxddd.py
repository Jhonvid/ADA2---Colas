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
        # Definir 5 colas con nombres de servicios
        self.servicios = {
            1: Cola(),  # Cola para "Seguro de Vida"
            2: Cola(),  # Cola para "Seguro de Carro"
            3: Cola(),  # Cola para "Seguro de Desastres Naturales"
            4: Cola(),  # Cola para "Seguro de Salud"
            5: Cola()   # Cola para "Seguro de Viajes"
        }

        # Contadores de atención para cada servicio
        self.numeros_atencion = {
            1: 0,  # Número de atención para "Seguro de Vida"
            2: 0,  # Número de atención para "Seguro de Carro"
            3: 0,  # Número de atención para "Seguro de Desastres Naturales"
            4: 0,  # Número de atención para "Seguro de Salud"
            5: 0   # Número de atención para "Seguro de Viajes"
        }

        # Nombres descriptivos de los servicios
        self.nombres_servicios = {
            1: "Seguro de Vida",
            2: "Seguro de Carro",
            3: "Seguro de Desastres Naturales",
            4: "Seguro de Salud",
            5: "Seguro de Viajes"
        }

    def llegada_cliente(self, servicio):
        if servicio in self.servicios:
            self.numeros_atencion[servicio] += 1
            numero_asignado = self.numeros_atencion[servicio]
            self.servicios[servicio].encolar(numero_asignado)
            print(f"Cliente {numero_asignado} asignado al servicio {self.nombres_servicios[servicio]}.")
        else:
            print("Servicio no válido.")

    def atender_cliente(self, servicio):
        if servicio in self.servicios:
            if not self.servicios[servicio].esta_vacia():
                cliente_atendido = self.servicios[servicio].desencolar()
                print(f"Atendiendo al cliente {cliente_atendido} del servicio {self.nombres_servicios[servicio]}.")
            else:
                print(f"No hay clientes en la cola del servicio {self.nombres_servicios[servicio]}.")
        else:
            print("Servicio no válido.")

    def ejecutar(self):
        while True:
            comando = input("Ingrese un comando (C para llegada, A para atender, S para salir): \n 1 para Seguro de Vida \n 2 para  Seguro de Carro \n 3 Seguro de Desastres Naturales \n 4 Seguro de Salud \n 5 Seguro de Viajes \n ").strip().upper()
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
