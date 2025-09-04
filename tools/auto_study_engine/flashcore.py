"""
flashcore.py - Sistema de gestión de flashcards
Módulo para manejar flashcards con persistencia en archivos JSON.
"""

import json
from typing import List, Dict, Any, TypedDict
ARCHIVO_DATOS = "data/mi_deck.json"


class Flashcard(TypedDict):
    """
    Estructura de datos para una flashcard.
    
    Attributes:
        pregunta (str): La pregunta de la flashcard
        respuesta (str): La respuesta correspondiente
        categoria (str): Categoría a la que pertenece la flashcard
    """
    pregunta: str
    respuesta: str
    categoria: str


def cargar_flashcards(nombre_archivo: str = ARCHIVO_DATOS) -> List[Flashcard]:
    """
    Carga las flashcards desde un archivo JSON.
    
    Args:
        nombre_archivo (str): Nombre del archivo JSON a cargar
        
    Returns:
        List[Flashcard]: Lista de flashcards cargadas, o lista vacía si el archivo no existe
        
    Raises:
        json.JSONDecodeError: Si el archivo JSON está corrupto
    """
    try:
        # Intentamos abrir y leer el archivo
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            
        # Validamos que los datos sean una lista
        if not isinstance(datos, list):
            print(f"Advertencia: El archivo {nombre_archivo} no contiene una lista válida")
            return []
            
        # Validamos cada flashcard individualmente
        flashcards_validadas = []
        for i, item in enumerate(datos):
            if isinstance(item, dict) and all(key in item for key in ['pregunta', 'respuesta', 'categoria']):
                flashcards_validadas.append(item)
            else:
                print(f"Advertencia: Elemento {i} no es una flashcard válida, se omite")
                
        return flashcards_validadas
        
    except FileNotFoundError:
        # El archivo no existe, devolvemos lista vacía
        print(f"Archivo {nombre_archivo} no encontrado. Se iniciará con lista vacía.")
        return []
        
    except json.JSONDecodeError as e:
        # El archivo existe pero está corrupto
        print(f"Error: El archivo {nombre_archivo} contiene JSON inválido: {e}")
        print("Se iniciará con lista vacía.")
        return []
        
    except PermissionError:
        # No tenemos permisos para leer el archivo
        print(f"Error: No tienes permisos para leer el archivo {nombre_archivo}")
        return []
        
    except Exception as e:
        # Cualquier otro error inesperado
        print(f"Error inesperado al cargar {nombre_archivo}: {e}")
        return []


def guardar_flashcards(flashcards: List[Flashcard], nombre_archivo: str = ARCHIVO_DATOS) -> bool:
    """
    Guarda las flashcards en un archivo JSON.
    
    Args:
        flashcards (List[Flashcard]): Lista de flashcards a guardar
        nombre_archivo (str): Nombre del archivo JSON donde guardar
        
    Returns:
        bool: True si se guardó exitosamente, False si hubo error
    """
    try:

        import os
        directorio = os.path.dirname(nombre_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio)
            print(f"✓ Directorio creado: {directorio}")
        
      
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            json.dump(flashcards, archivo, indent=4, ensure_ascii=False)
            
        print(f"✓ Flashcards guardadas exitosamente en {nombre_archivo}")
        return True
        
    except PermissionError:
        # No tenemos permisos para escribir
        print(f"Error: No tienes permisos para escribir en {nombre_archivo}")
        return False
        
    except OSError as e:
        # Problemas del sistema operativo (disco lleno, ruta inválida, etc.)
        print(f"Error del sistema al guardar {nombre_archivo}: {e}")
        return False
        
    except TypeError as e:
        # Los datos no se pueden serializar a JSON
        print(f"Error: Los datos no se pueden convertir a JSON: {e}")
        return False
        
    except Exception as e:
        # Cualquier otro error inesperado
        print(f"Error inesperado al guardar {nombre_archivo}: {e}")
        return False


# Funciones auxiliares útiles

def crear_flashcard(pregunta: str, respuesta: str, categoria: str) -> Flashcard:
    """
    Crea una nueva flashcard con validación básica.
    
    Args:
        pregunta (str): La pregunta de la flashcard
        respuesta (str): La respuesta correspondiente  
        categoria (str): Categoría de la flashcard
        
    Returns:
        Flashcard: Nueva flashcard creada
        
    Raises:
        ValueError: Si algún parámetro está vacío
    """
    # Validaciones básicas
    if not pregunta.strip():
        raise ValueError("La pregunta no puede estar vacía")
    if not respuesta.strip():
        raise ValueError("La respuesta no puede estar vacía")
    if not categoria.strip():
        raise ValueError("La categoría no puede estar vacía")
    
    return Flashcard(
        pregunta=pregunta.strip(),
        respuesta=respuesta.strip(),
        categoria=categoria.strip()
    )


def obtener_categorias(flashcards: List[Flashcard]) -> List[str]:
    """
    Obtiene una lista única de todas las categorías existentes.
    
    Args:
        flashcards (List[Flashcard]): Lista de flashcards
        
    Returns:
        List[str]: Lista ordenada de categorías únicas
    """
    categorias = set(flashcard['categoria'] for flashcard in flashcards)
    return sorted(categorias)


def filtrar_por_categoria(flashcards: List[Flashcard], categoria: str) -> List[Flashcard]:
    """
    Filtra flashcards por categoría específica.
    
    Args:
        flashcards (List[Flashcard]): Lista completa de flashcards
        categoria (str): Categoría a filtrar
        
    Returns:
        List[Flashcard]: Flashcards de la categoría especificada
    """
    return [fc for fc in flashcards if fc['categoria'].lower() == categoria.lower()]


# Ejemplo de uso
if __name__ == "__main__":
    # Crear algunas flashcards de ejemplo
    flashcards_ejemplo = [
        crear_flashcard("¿Qué es Python?", "Un lenguaje de programación", "Programación"),
        crear_flashcard("¿Capital de Francia?", "París", "Geografía"),
        crear_flashcard("¿Qué es una lista?", "Una colección ordenada de elementos", "Programación")
    ]
    
    # Guardar las flashcards
    if guardar_flashcards(flashcards_ejemplo, "data/mi_deck.json"):
        print("Ejemplo creado exitosamente")
    
    # Cargar y mostrar
    flashcards_cargadas = cargar_flashcards("ejemplo_flashcards.json")
    print(f"Se cargaron {len(flashcards_cargadas)} flashcards")
    
    # Mostrar categorías disponibles
    categorias = obtener_categorias(flashcards_cargadas)
    print(f"Categorías disponibles: {categorias}")