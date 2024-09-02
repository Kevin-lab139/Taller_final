class cine: 
     def ver_mis_reservas(self):
        print("Mis reservas:")
        if len(self.RESERVAS) == 0:
            print("No hay reservas")
        else:
            for asientos, datos in self.RESERVAS.items():
                print(f"Asientos {asientos}: Usuario {datos['usuario']}")