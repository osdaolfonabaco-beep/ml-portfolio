"""
Módulo agent_claude.py
Generador de flashcards educativas a partir de código Python usando Claude AI.

Este módulo proporciona funcionalidades para analizar código Python y generar
flashcards educativas que ayuden a comprender los conceptos más importantes
del código analizado.
"""

import os
import json
from typing import List, Dict, Any
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def generar_flashcards_desde_codigo(ruta_archivo: str) -> List[Dict[str, str]]:
    """
    Genera flashcards educativas analizando código Python desde un archivo.
    
    Esta función lee un archivo Python, construye un prompt optimizado para
    que Claude analice el código, y devuelve flashcards educativas sobre
    los conceptos más importantes encontrados.
    
    Args:
        ruta_archivo (str): Ruta al archivo Python (.py) que se va a analizar.
        
    Returns:
        List[Dict[str, str]]: Lista de flashcards, cada una con los campos:
            - 'pregunta': La pregunta de la flashcard
            - 'respuesta': La respuesta correcta
            - 'explicacion': Explicación detallada del concepto
            - 'categoria': Categoría del concepto (ej: 'estructuras_datos')
            
    Raises:
        FileNotFoundError: Si el archivo especificado no existe.
        IOError: Si hay problemas al leer el archivo.
        ValueError: Si el archivo no tiene extensión .py o está vacío.
        
    Example:
        >>> flashcards = generar_flashcards_desde_codigo("mi_script.py")
        >>> print(f"Se generaron {len(flashcards)} flashcards")
        >>> print(flashcards[0]['pregunta'])
    """
    # Validar extensión del archivo
    if not ruta_archivo.endswith('.py'):
        raise ValueError(f"El archivo debe tener extensión .py, recibido: {ruta_archivo}")
    
    try:
        # Leer el contenido del archivo
        contenido_codigo = _leer_archivo_python(ruta_archivo)
        
        # Construir el prompt optimizado para Claude
        prompt_claude = _construir_prompt_analisis_codigo(contenido_codigo, ruta_archivo)
        
        # Por ahora simulamos la respuesta de Claude
        # En producción, aquí iría la llamada real a la API
        logger.info(f"Prompt construido para análisis de {ruta_archivo}")
        logger.info(f"Longitud del código: {len(contenido_codigo)} caracteres")
        
        # Simular respuesta de Claude
        flashcards_simuladas = _simular_respuesta_claude(contenido_codigo, ruta_archivo)
        
        logger.info(f"Generadas {len(flashcards_simuladas)} flashcards para {ruta_archivo}")
        return flashcards_simuladas
        
    except FileNotFoundError as e:
        logger.error(f"Archivo no encontrado: {ruta_archivo}")
        raise FileNotFoundError(f"No se pudo encontrar el archivo: {ruta_archivo}") from e
        
    except IOError as e:
        logger.error(f"Error de E/S al leer {ruta_archivo}: {str(e)}")
        raise IOError(f"Error al leer el archivo {ruta_archivo}: {str(e)}") from e
        
    except Exception as e:
        logger.error(f"Error inesperado procesando {ruta_archivo}: {str(e)}")
        raise


def _leer_archivo_python(ruta_archivo: str) -> str:
    """
    Lee el contenido de un archivo Python con manejo robusto de errores.
    
    Args:
        ruta_archivo (str): Ruta al archivo Python.
        
    Returns:
        str: Contenido del archivo.
        
    Raises:
        FileNotFoundError: Si el archivo no existe.
        IOError: Si hay problemas de lectura.
        ValueError: Si el archivo está vacío.
    """
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"El archivo {ruta_archivo} no existe")
    
    if not os.path.isfile(ruta_archivo):
        raise IOError(f"La ruta {ruta_archivo} no apunta a un archivo válido")
    
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            
        if not contenido.strip():
            raise ValueError(f"El archivo {ruta_archivo} está vacío")
            
        return contenido
        
    except UnicodeDecodeError as e:
        logger.warning(f"Error de codificación UTF-8, intentando con latin-1: {e}")
        try:
            with open(ruta_archivo, 'r', encoding='latin-1') as archivo:
                return archivo.read()
        except Exception as fallback_error:
            raise IOError(f"No se pudo leer el archivo con ninguna codificación: {fallback_error}") from e


def _construir_prompt_analisis_codigo(contenido_codigo: str, nombre_archivo: str) -> str:
    """
    Construye un prompt optimizado para que Claude analice código Python.
    
    Args:
        contenido_codigo (str): El código fuente a analizar.
        nombre_archivo (str): Nombre del archivo para contexto.
        
    Returns:
        str: Prompt estructurado y específico para Claude.
    """
    prompt = f"""
Actúa como un experto instructor de programación en Python. Analiza el siguiente código del archivo '{nombre_archivo}' y genera exactamente 3-5 flashcards educativas sobre los conceptos más importantes y relevantes del código.

**CÓDIGO A ANALIZAR:**
```python
{contenido_codigo}
```

**INSTRUCCIONES ESPECÍFICAS:**
1. Identifica los conceptos de programación más importantes en el código
2. Prioriza conceptos que sean educativos y transferibles a otros proyectos
3. Incluye tanto conceptos básicos como avanzados según corresponda
4. Enfócate en patrones, estructuras de datos, algoritmos, o buenas prácticas presentes

**FORMATO DE RESPUESTA REQUERIDO:**
Devuelve ÚNICAMENTE un JSON válido con esta estructura:
```json
[
    {{
        "pregunta": "¿Pregunta clara y específica sobre un concepto del código?",
        "respuesta": "Respuesta concisa y precisa",
        "explicacion": "Explicación detallada con ejemplo si es necesario",
        "categoria": "categoria_del_concepto"
    }}
]
```

**CATEGORÍAS PERMITIDAS:**
- estructuras_datos
- algoritmos
- programacion_orientada_objetos
- manejo_errores
- buenas_practicas
- patrones_diseno
- sintaxis_python

**CRITERIOS DE CALIDAD:**
- Preguntas específicas al código analizado
- Respuestas técnicamente correctas
- Explicaciones que agreguen valor educativo
- Conceptos aplicables más allá de este código específico

Genera las flashcards ahora:
"""
    return prompt


def _simular_respuesta_claude(contenido_codigo: str, ruta_archivo: str) -> List[Dict[str, str]]:
    """
    Simula la respuesta que devolvería Claude AI basándose en el código.
    
    Esta función genera flashcards de ejemplo realistas basadas en 
    patrones comunes de código Python.
    
    Args:
        contenido_codigo (str): El código fuente analizado.
        ruta_archivo (str): Nombre del archivo para personalizar ejemplos.
        
    Returns:
        List[Dict[str, str]]: Lista de flashcards simuladas.
    """
    # Análisis básico del código para generar flashcards más realistas
    tiene_clases = 'class ' in contenido_codigo
    tiene_funciones = 'def ' in contenido_codigo
    tiene_imports = 'import ' in contenido_codigo or 'from ' in contenido_codigo
    tiene_excepciones = 'try:' in contenido_codigo or 'except' in contenido_codigo
    tiene_listas = '[' in contenido_codigo and ']' in contenido_codigo
    tiene_diccionarios = '{' in contenido_codigo and '}' in contenido_codigo
    
    flashcards = []
    
    if tiene_funciones:
        flashcards.append({
            "pregunta": "¿Qué es una función en Python y cuál es su propósito principal?",
            "respuesta": "Una función es un bloque de código reutilizable que realiza una tarea específica, definida con 'def'",
            "explicacion": "Las funciones permiten modularizar el código, evitar repetición y hacer el programa más mantenible. Se definen una vez y pueden llamarse múltiples veces con diferentes parámetros.",
            "categoria": "buenas_practicas"
        })
    
    if tiene_clases:
        flashcards.append({
            "pregunta": "¿Qué representa una clase en programación orientada a objetos?",
            "respuesta": "Una clase es una plantilla que define atributos y métodos para crear objetos",
            "explicacion": "Las clases encapsulan datos (atributos) y comportamientos (métodos) relacionados. Permiten crear múltiples instancias (objetos) con las mismas características pero valores diferentes.",
            "categoria": "programacion_orientada_objetos"
        })
    
    if tiene_excepciones:
        flashcards.append({
            "pregunta": "¿Por qué es importante el manejo de excepciones con try/except?",
            "respuesta": "Permite capturar y manejar errores sin que el programa se termine abruptamente",
            "explicacion": "El manejo de excepciones hace que los programas sean más robustos y proporciona una mejor experiencia de usuario al manejar errores de forma controlada.",
            "categoria": "manejo_errores"
        })
    
    if tiene_listas or tiene_diccionarios:
        estructura = "listas y diccionarios" if tiene_listas and tiene_diccionarios else ("listas" if tiene_listas else "diccionarios")
        flashcards.append({
            "pregunta": f"¿Cuál es la diferencia principal entre {estructura} en Python?",
            "respuesta": "Las listas almacenan elementos ordenados por índice numérico, los diccionarios usan claves para acceso directo",
            "explicacion": "Las listas son estructuras ordenadas ideales para secuencias, mientras que los diccionarios permiten acceso rápido por clave y son perfectos para mapear relaciones clave-valor.",
            "categoria": "estructuras_datos"
        })
    
    if tiene_imports:
        flashcards.append({
            "pregunta": "¿Qué ventaja proporcionan los imports en Python?",
            "respuesta": "Permiten reutilizar código de otros módulos y bibliotecas sin reescribirlo",
            "explicacion": "Los imports facilitan la modularidad, reutilización de código y acceso a la vasta biblioteca estándar de Python y paquetes de terceros.",
            "categoria": "buenas_practicas"
        })
    
    # Si no hay suficientes flashcards específicas, agregar una genérica
    if len(flashcards) < 3:
        flashcards.append({
            "pregunta": "¿Cuál es una buena práctica al escribir código Python legible?",
            "respuesta": "Usar nombres descriptivos para variables y funciones, y seguir las convenciones PEP 8",
            "explicacion": "El código legible es más fácil de mantener, debuggear y colaborar. PEP 8 establece convenciones estándar que hacen el código consistente en la comunidad Python.",
            "categoria": "buenas_practicas"
        })
    
    # Retornar solo las primeras 5 flashcards máximo
    return flashcards[:5]


# Función de utilidad para testing y debugging
def mostrar_ejemplo_uso():
    """
    Muestra un ejemplo de uso del módulo para propósitos de testing.
    """
    print("=== Ejemplo de uso del módulo agent_claude.py ===")
    print("Código de ejemplo:")
    print("flashcards = generar_flashcards_desde_codigo('mi_archivo.py')")
    print("for card in flashcards:")
    print("    print(f'P: {card[\"pregunta\"]}\\nR: {card[\"respuesta\"]}\\n')")

# === NUEVA FUNCIÓN PARA EL SISTEMA PRINCIPAL ===
def generate_flashcards_from_code() -> List[Dict[str, str]]:
    """
    Función principal para generar flashcards desde archivos de código.
    Esta es la función que llama test_quiz.py y el GitHub Action.
    
    Returns:
        List[Dict[str, str]]: Lista de todas las flashcards generadas
    """
    import os
    
    # Obtener la ruta absoluta del directorio raíz del proyecto
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(current_dir, '../..'))
    
    # DEBUG: Verificar rutas
    print(f"🔍 DEBUG: Directorio actual: {current_dir}")
    print(f"🔍 DEBUG: Root directory: {root_dir}")
    
    file_paths = [
        os.path.join(root_dir, 'foundations', 'python_advanced', 'lista_compras.py'),
        os.path.join(root_dir, 'foundations', 'python_advanced', 'test_lista_compras.py')
    ]
    
    all_flashcards = []
    
    for file_path in file_paths:
        try:
            print(f"🔍 DEBUG: Verificando {file_path}")
            if os.path.exists(file_path):
                print(f"✅ DEBUG: Archivo encontrado: {os.path.basename(file_path)}")
                flashcards = generar_flashcards_desde_codigo(file_path)
                all_flashcards.extend(flashcards)
                logger.info(f"✓ Generadas {len(flashcards)} flashcards desde {os.path.basename(file_path)}")
            else:
                logger.warning(f"⚠ Archivo no encontrado: {file_path}")
                print(f"❌ DEBUG: Archivo NO existe: {file_path}")
        except Exception as e:
            logger.error(f"✗ Error procesando {file_path}: {str(e)}")
            print(f"💥 ERROR: {str(e)}")
    
    print(f"📊 DEBUG: Total flashcards generadas: {len(all_flashcards)}")
    return all_flashcards


# === FUNCIÓN DE UTILIDAD PARA DEBUG ===
def debug_file_paths():
    """Función para debuggear las rutas de archivo"""
    import os
    current_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.abspath(os.path.join(current_dir, '../..'))
    
    print("=== DEBUG DE RUTAS ===")
    print(f"Directorio actual del script: {current_dir}")
    print(f"Directorio raíz del proyecto: {root_dir}")
    
    test_path = os.path.join(root_dir, 'foundations', 'python_advanced', 'lista_compras.py')
    print(f"Ruta completa a lista_compras.py: {test_path}")
    print(f"¿Existe el archivo? {os.path.exists(test_path)}")
    
    # Listar contenido del directorio
    python_advanced_dir = os.path.join(root_dir, 'foundations', 'python_advanced')
    if os.path.exists(python_advanced_dir):
        print(f"Archivos en python_advanced/: {os.listdir(python_advanced_dir)}")


if __name__ == "__main__":
    # Ejemplo básico de testing
    mostrar_ejemplo_uso()