class Cine:
    def __init__(self):
        self.SALA = []  # Representación de la sala (se creará en la opción 1)
        self.RESERVAS = {}   # Diccionario para almacenar reservas (clave: asiento, valor: usuario)

    def crear_sala(self):
        num_filas = int(input("Ingrese el número de filas: "))
        num_columnas = int(input("Ingrese el número de columnas: "))
        self.num_asientos = num_filas * num_columnas
        self.SALA = [[str(i * num_columnas + j + 1) for j in range(num_columnas)] for i in range(num_filas)]
        print("Sala creada:")
        for fila in self.SALA:
            print(" ".join(fila))

    def ver_sala(self):
        print("Sala:")
        for fila in self.SALA:
            print(" ".join(fila))
        
        while True:
            asiento_seleccionado = input("Seleccione los asientos (separados por comas): ").split(",")
            # Validar asientos seleccionados
            if all(self.validar_asiento(asiento) for asiento in asiento_seleccionado):
                return asiento_seleccionado
            else:
                print("Error: Por favor seleccione asientos válidos.")

    def validar_asiento(self, asiento):
        # Verificar si el asiento está dentro del rango válido
        if not asiento.isdigit() or int(asiento) < 1 or int(asiento) > self.num_asientos:
            return False
        
        # Verificar si el asiento ya está ocupado
        for fila in self.SALA:
            if asiento in fila:
                return fila[fila.index(asiento)] != "X"
        
        return False

    def realizar_reserva(self, asiento, usuario):
        asientos_tupla = tuple(asiento)
        self.RESERVAS[asientos_tupla] = {"usuario": usuario}

        # Marcar los asientos como ocupados en la sala
        for fila in self.SALA:
            for i, num in enumerate(fila):
                if num in asiento:
                    fila[i] = "X"

        print("Reserva realizada con éxito.")

    def ver_mis_reservas(self):
        print("Mis reservas:")
        if len(self.RESERVAS) == 0:
            print("No hay reservas")
        else:
            for asientos, datos in self.RESERVAS.items():
                print(f"Asientos {asientos}: Usuario {datos['usuario']}")

if __name__ == "__main__":
    cine = Cine()
    while True:
        print("\nBienvenido al Teatro Apolo")
        print("1. Crear sala")
        print("2. Ver sala y seleccionar asiento")
        print("3. Realizar reserva")
        print("4. Ver mis reservas")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cine.crear_sala()
        elif opcion == "2":
            asiento_seleccionado = cine.ver_sala()
        elif opcion == "3":
            usuario = input("Ingrese su nombre: ")
            cine.realizar_reserva(asiento_seleccionado, usuario)
        elif opcion == "4":
            cine.ver_mis_reservas()
        elif opcion == "5":
            print("Gracias por usar la aplicación")
            break
        else:
            print("Opción no válida")