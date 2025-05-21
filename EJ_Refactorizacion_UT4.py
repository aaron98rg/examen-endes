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

    @staticmethod
    def crear_receta():
        ingredientes = []
        pasos = []
        plato = input("¿Que plato quieres elaborar?: ")
        num_ingredientes = int(input("Cuantos ingredientes tiene tu plato?: "))
        for i in range(num_ingredientes):
            ingrediente = input("Agrega ingrediente:")
            ingredientes.append(ingrediente)
        
        for i in range(3):
            paso = input("Agrega paso: ")
            pasos.append(paso)
        print(f"Ingredientes para {plato}: ")
        for i in range(len(ingredientes)):
            print(f"* {ingredientes[i]}")
        print("-Pasos a seguir: ")
        for i in range(len(pasos)):
            print(f" {i}- {pasos[i]}")

# Función principal
def main():
    recetario = []
    while True:
        print("1.Crear receta.")
        print("2.Mostrar receta.")
        print("3.Salir.")

        opciones = int(input("Elige una opcion: "))
        match opciones:
            
            case 1:
                tipo = input("Que tipo de receta quieres crear?")
                if tipo == "vegetariana":
                    print("RECETA VEGETARIANA")
                    receta = utilidades.crear_receta()
                    recetario.append(receta)
                elif tipo =="carnivora":
                    print("RECETA CARNIVORA")
                    receta = utilidades.crear_receta()
                    recetario.append(receta)


            case 2:
                utilidades.imprimir_receta(recetario)
            
            case 3:
                break

            case _: 
                raise ValueError("Opcion no valida")


# Ejecutar el programa
if __name__ == "__main__":
    main()
