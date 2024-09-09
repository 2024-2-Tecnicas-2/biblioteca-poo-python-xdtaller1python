class Revista(Publicacion):
    def __init__(self, titulo, anio_publicacion, num_revista, nombre_revista):
        super().__init__(titulo, anio_publicacion)
        self.num_revista = num_revista
        self.nombre_revista = nombre_revista

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número de revista: {self.num_revista}")
        print(f"Nombre de la revista: {self.nombre_revista}")

    
