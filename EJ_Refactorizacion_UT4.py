from abc import ABC, abstractmethod

# Clase abstracta para representar una receta
class receta(ABC):
    def __init__(self, nombre, ingrediente, pasos):
        self.nombre = nombre  # nombre
        self.ingrediente = ingrediente  # ingredientes
        self.pasos = pasos  # pasos

    
    def mostrar_receta(self):
        print(f"Receta NO vegetariana: {self.nombre}")
        print("Ingredientes:")
        for ing in self.ingrediente:
            print(f"- {ing}")
        print("Pasos:")
        for paso in self.pasos:
            print(f"{paso}")


# Clase para recetas vegetarianas
class recVegetariana(receta):
    def mostrar(self):
        self.mostrar_receta()




# Clase para recetas no vegetarianas
class recNoVegetariana(receta):
    def mostrar(self):
        self.mostrar_receta()

    


# Clase con utilidades del restaurante
class utilidades:
    @staticmethod
    def imprimir_receta(receta):
        print("====================================")
        receta.mostrar()
        print("====================================")

    @staticmethod
    def mostrar_lista_ingredientes(lista):
        for ingrediente in lista:
            print(f"* {ingrediente}")

# Función principal
def main():
    receta1 = recVegetariana("Ensalada César", ["lechuga", "queso", "pan tostado", "salsa"], ["Lavar", "Mezclar", "Servir"])
    receta2 = recNoVegetariana("Pollo al horno", ["pollo", "patatas", "ajo", "aceite"], ["Preparar", "Hornear", "Servir"])
    
    # Duplicación de código al imprimir
    print("== Mostrar recetas ==")
    utilidades.imprimir_receta(receta1)
    utilidades.imprimir_receta(receta2)

    # Código duplicado para mostrar ingredientes
    print("Ingredientes de Ensalada César:")
    for ing in receta1.ingrediente:
        print(f"* {ing}")
    
    print("Ingredientes de Pollo al horno:")
    for ing in receta2.ingrediente:
        print(f"* {ing}")


# Ejecutar el programa
if __name__ == "__main__":
    main()
