"""
Sistema profesional de lista de compras con persistencia JSON.
Incluye type hints, manejo de errores, y funciones modulares.
Ideal para demostrar habilidades técnicas en entrevistas.
"""
import json
import os
from typing import List, Dict, Callable, Optional

# Type aliases para claridad profesional
Item = Dict[str, float | str]
ListaCompras = List[Item]

ARCHIVO_DATOS = "lista_compras.json"

def cargar_lista(ruta_archivo: str = ARCHIVO_DATOS) -> ListaCompras:
    """
    Carga la lista de compras desde un archivo JSON.
    
    Args:
        ruta_archivo (str): Ruta del archivo JSON. Por defecto 'lista_compras.json'.
    
    Returns:
        ListaCompras: Lista de items cargados desde el archivo, o lista vacía si el archivo no existe.
    
    Raises:
        json.JSONDecodeError: Si el archivo existe pero tiene formato JSON inválido.
    """
    try:
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        return []
    except json.JSONDecodeError as e:
        print(f"❌ Error cargando datos: Archivo JSON corrupto. Creando nueva lista. Error: {e}")
        return []

def guardar_lista(lista: ListaCompras, ruta_archivo: str = ARCHIVO_DATOS) -> None:
    """
    Guarda la lista de compras en un archivo JSON.
    
    Args:
        lista (ListaCompras): Lista de items a guardar.
        ruta_archivo (str): Ruta del archivo JSON. Por defecto 'lista_compras.json'.
    """
    try:
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(lista, archivo, indent=2, ensure_ascii=False)
        print(f"✅ Lista guardada exitosamente en {ruta_archivo}")
    except IOError as e:
        print(f"❌ Error guardando archivo: {e}")

def agregar_item(lista: ListaCompras, nombre: str, precio: float, cantidad: int = 1) -> None:
    """
    Agrega un item a la lista de compras.
    
    Args:
        lista (ListaCompras): Lista donde se agregará el item.
        nombre (str): Nombre del producto.
        precio (float): Precio unitario del producto.
        cantidad (int, optional): Cantidad del producto. Default: 1.
    
    Raises:
        ValueError: Si el precio o cantidad son negativos.
    """
    if precio < 0:
        raise ValueError("El precio no puede ser negativo")
    if cantidad < 1:
        raise ValueError("La cantidad debe ser al menos 1")
    
    lista.append({
        "nombre": nombre.strip().title(),
        "precio": round(precio, 2),
        "cantidad": cantidad
    })
    print(f"✅ Item agregado: {nombre}")

def eliminar_item(lista: ListaCompras, indice: int) -> None:
    """
    Elimina un item de la lista por índice.
    
    Args:
        lista (ListaCompras): Lista de la que se eliminará el item.
        indice (int): Índice del item a eliminar (base 0).
    
    Raises:
        IndexError: Si el índice está fuera de rango.
    """
    if indice < 0 or indice >= len(lista):
        raise IndexError("Índice fuera de rango")
    
    item_eliminado = lista.pop(indice)
    print(f"❌ Item eliminado: {item_eliminado['nombre']}")

def calcular_total(lista: ListaCompras) -> float:
    """
    Calcula el total de la lista de compras.
    
    Args:
        lista (ListaCompras): Lista de items.
    
    Returns:
        float: Total calculado (precio * cantidad para cada item).
    """
    return sum(item["precio"] * item["cantidad"] for item in lista)

def mostrar_lista(lista: ListaCompras) -> None:
    """
    Muestra la lista de compras formateada.
    
    Args:
        lista (ListaCompras): Lista de items a mostrar.
    """
    if not lista:
        print("📝 La lista de compras está vacía")
        return
    
    print("\n🛒 LISTA DE COMPRAS")
    print("-" * 40)
    for i, item in enumerate(lista):
        print(f"{i+1}. {item['nombre']} - ${item['precio']:.2f} x {item['cantidad']} = ${item['precio'] * item['cantidad']:.2f}")
    print("-" * 40)
    print(f"💰 TOTAL: ${calcular_total(lista):.2f}\n")

def aplicar_descuento(item: Item, porcentaje: float = 10.0) -> None:
    """
    Aplica un descuento porcentual a un item.
    
    Args:
        item (Item): Item al que se aplicará el descuento.
        porcentaje (float, optional): Porcentaje de descuento. Default: 10.0.
    """
    descuento = item["precio"] * (porcentaje / 100)
    item["precio"] = round(item["precio"] - descuento, 2)
    print(f"🎯 Descuento del {porcentaje}% aplicado a {item['nombre']}")

def main():
    """Función principal con menú interactivo."""
    lista = cargar_lista()
    
    while True:
        print("\n" + "="*50)
        print("🛒 SISTEMA DE LISTA DE COMPRAS PROFESIONAL")
        print("="*50)
        print("1. Agregar item")
        print("2. Ver lista")
        print("3. Eliminar item")
        print("4. Aplicar descuento a item")
        print("5. Calcular total")
        print("6. Guardar y salir")
        print("7. Salir sin guardar")
        print("="*50)
        
        opcion = input("Seleccione una opción (1-7): ").strip()
        
        try:
            if opcion == "1":
                nombre = input("Nombre del producto: ")
                precio = float(input("Precio unitario: "))
                cantidad = int(input("Cantidad: "))
                agregar_item(lista, nombre, precio, cantidad)
                
            elif opcion == "2":
                mostrar_lista(lista)
                
            elif opcion == "3":
                mostrar_lista(lista)
                if lista:
                    indice = int(input("Número del item a eliminar: ")) - 1
                    eliminar_item(lista, indice)
            
            elif opcion == "4":
                mostrar_lista(lista)
                if lista:
                    indice = int(input("Número del item para descuento: ")) - 1
                    porcentaje = float(input("Porcentaje de descuento: "))
                    aplicar_descuento(lista[indice], porcentaje)
            
            elif opcion == "5":
                print(f"\n💰 TOTAL DE LA LISTA: ${calcular_total(lista):.2f}")
            
            elif opcion == "6":
                guardar_lista(lista)
                print("👋 ¡Hasta pronto!")
                break
            
            elif opcion == "7":
                print("👋 ¡Hasta pronto! (Cambios no guardados)")
                break
            
            else:
                print("❌ Opción no válida. Intente de nuevo.")
                
        except ValueError as e:
            print(f"❌ Error de valor: {e}")
        except IndexError as e:
            print(f"❌ Error de índice: {e}")
        except Exception as e:
            print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    main()
# Comentario de prueba para activar workflow
# Comentario de prueba para activar workflow
# Comentario de prueba para activar workflow
