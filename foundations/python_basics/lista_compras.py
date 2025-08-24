
# lista_compras.py
def agregar_item(lista, item, cantidad):
    """
    Agrega un item al diccionario de la lista de compras.
    Si el item ya existe, suma la cantidad nueva a la existente.
    
    Args:
        lista (dict): Diccionario que representa la lista de compras.
        item (str): Nombre del item a agregar.
        cantidad (int): Cantidad del item.
    
    Returns:
        dict: Lista actualizada.
    """
    if item in lista:
        lista[item] += cantidad  # Suma cantidades si el item existe
    else:
        lista[item] = cantidad  # Crea nueva entrada si no existe
    return lista

def eliminar_item(lista, item):
    """
    Elimina un item del diccionario si existe.
    
    Args:
        lista (dict): Diccionario de la lista de compras.
        item (str): Item a eliminar.
    
    Returns:
        dict: Lista actualizada.
    """
    if item in lista:
        del lista[item]
        print(f"'{item}' eliminado.")
    else:
        print(f"Error: '{item}' no está en la lista.")
    return lista

def ver_lista(lista):
    """
    Imprime la lista de compras actual con formato claro.
    
    Args:
        lista (dict): Diccionario de la lista de compras.
    """
    if not lista:
        print("La lista está vacía.")
    else:
        print("\n--- Lista de Compras ---")
        for item, cantidad in lista.items():
            print(f"- {item}: {cantidad}")

def main():
    """
    Función principal que ejecuta el menú interactivo.
    """
    lista_compras = {}  # Diccionario vacío para almacenar items
    while True:
        print("\nOpciones:")
        print("1. Agregar item")
        print("2. Eliminar item")
        print("3. Ver lista")
        print("4. Salir")
        
        opcion = input("Selecciona una opción (1-4): ").strip()
        
        if opcion == "1":
            try:
                item = input("Nombre del item: ").strip().lower()
                cantidad = int(input("Cantidad: "))
                if cantidad <= 0:
                    print("Error: La cantidad debe ser positiva.")
                    continue
                lista_compras = agregar_item(lista_compras, item, cantidad)
                print(f"✅ Added {cantidad} de {item}.")
            except ValueError:
                print("Error: La cantidad debe ser un número entero.")
        
        elif opcion == "2":
            item = input("Item a eliminar: ").strip().lower()
            lista_compras = eliminar_item(lista_compras, item)
        
        elif opcion == "3":
            ver_lista(lista_compras)
        
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        
        else:
            print("Error: Opción no válida. Elige 1-4.")

if __name__ == "__main__":
    main()