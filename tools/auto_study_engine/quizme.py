"""
Módulo de sistema de quiz para flashcards educativas.

Este módulo proporciona funcionalidad para ejecutar quizzes interactivos
basados en flashcards, con soporte para múltiples intentos, puntuación
y retroalimentación educativa.

Author: Sistema Educativo
Version: 1.0.0
"""

from typing import List, Dict, Any, Tuple
import random


class QuizError(Exception):
    """Excepción personalizada para errores del sistema de quiz."""
    pass


def validar_flashcard(flashcard: Dict[str, Any], indice: int) -> None:
    """
    Valida que una flashcard tenga la estructura correcta.
    
    Args:
        flashcard: Diccionario con los datos de la flashcard
        indice: Índice de la flashcard en el deck (para mensajes de error)
    
    Raises:
        QuizError: Si la flashcard no tiene la estructura requerida
    """
    campos_requeridos = ['pregunta', 'respuesta', 'categoria']
    
    for campo in campos_requeridos:
        if campo not in flashcard:
            raise QuizError(f"Flashcard #{indice + 1} no tiene el campo requerido: '{campo}'")
    
    if not isinstance(flashcard['pregunta'], str) or not flashcard['pregunta'].strip():
        raise QuizError(f"Flashcard #{indice + 1} tiene una pregunta inválida")
    
    if not isinstance(flashcard['respuesta'], str) or not flashcard['respuesta'].strip():
        raise QuizError(f"Flashcard #{indice + 1} tiene una respuesta inválida")


def procesar_respuesta_usuario(respuesta_usuario: str, respuesta_correcta: str) -> bool:
    """
    Compara la respuesta del usuario con la respuesta correcta.
    
    Args:
        respuesta_usuario: Respuesta ingresada por el usuario
        respuesta_correcta: Respuesta correcta de la flashcard
    
    Returns:
        bool: True si la respuesta es correcta, False en caso contrario
    """
    # Normalizar respuestas: eliminar espacios y convertir a minúsculas
    respuesta_usuario_norm = respuesta_usuario.strip().lower()
    respuesta_correcta_norm = respuesta_correcta.strip().lower()
    
    return respuesta_usuario_norm == respuesta_correcta_norm


def ejecutar_pregunta(flashcard: Dict[str, Any], numero_pregunta: int) -> Tuple[float, bool]:
    """
    Ejecuta una pregunta individual con lógica de 2 intentos.
    
    Args:
        flashcard: Diccionario con los datos de la pregunta
        numero_pregunta: Número de la pregunta actual (para display)
    
    Returns:
        Tuple[float, bool]: (puntos_obtenidos, respondio_correctamente)
    """
    pregunta = flashcard['pregunta']
    respuesta_correcta = flashcard['respuesta']
    explicacion = flashcard.get('explicacion', '')  # Acceso seguro con get()
    categoria = flashcard['categoria']
    
    print(f"\n{'='*50}")
    print(f"Pregunta {numero_pregunta} | Categoría: {categoria}")
    print(f"{'='*50}")
    print(f"❓ {pregunta}")
    
    # Primer intento
    respuesta_usuario = input("\n💭 Tu respuesta: ").strip()
    
    if procesar_respuesta_usuario(respuesta_usuario, respuesta_correcta):
        print("✅ ¡Correcto! Excelente trabajo.")
        if explicacion:
            print(f"💡 Información adicional: {explicacion}")
        return 1.0, True
    
    # Primer intento fallido
    print("❌ Incorrecto. Te queda 1 intento.")
    
    # Segundo intento
    respuesta_usuario = input("💭 Tu respuesta (último intento): ").strip()
    
    if procesar_respuesta_usuario(respuesta_usuario, respuesta_correcta):
        print("✅ ¡Correcto en el segundo intento!")
        if explicacion:
            print(f"💡 Información adicional: {explicacion}")
        return 0.5, True
    
    # Segundo intento fallido - revelar respuesta
    print(f"❌ Incorrecto. La respuesta correcta era: '{respuesta_correcta}'")
    if explicacion:
        print(f"💡 Explicación: {explicacion}")
    
    return 0.0, False


def mostrar_resumen_final(puntuacion_total: float, total_preguntas: int, 
                         correctas: int, parcialmente_correctas: int) -> None:
    """
    Muestra el resumen final del quiz con estadísticas detalladas.
    
    Args:
        puntuacion_total: Puntuación total obtenida
        total_preguntas: Total de preguntas del quiz
        correctas: Preguntas respondidas correctamente en primer intento
        parcialmente_correctas: Preguntas respondidas correctamente en segundo intento
    """
    porcentaje = (puntuacion_total / total_preguntas) * 100 if total_preguntas > 0 else 0
    incorrectas = total_preguntas - correctas - parcialmente_correctas
    
    print(f"\n{'='*60}")
    print("🎯 RESUMEN FINAL DEL QUIZ")
    print(f"{'='*60}")
    print(f"📊 Puntuación total: {puntuacion_total:.1f}/{total_preguntas} ({porcentaje:.1f}%)")
    print(f"✅ Correctas (1er intento): {correctas}")
    print(f"⚠️  Correctas (2do intento): {parcialmente_correctas}")
    print(f"❌ Incorrectas: {incorrectas}")
    
    # Retroalimentación motivacional
    if porcentaje >= 90:
        print("\n🏆 ¡Excelente! Dominas muy bien el material.")
    elif porcentaje >= 70:
        print("\n👍 ¡Buen trabajo! Tienes un buen entendimiento.")
    elif porcentaje >= 50:
        print("\n📚 Puedes mejorar. Te recomiendo repasar el material.")
    else:
        print("\n💪 Sigue estudiando. La práctica hace al maestro.")


def iniciar_quiz(deck: List[Dict[str, Any]]) -> None:
    """
    Inicia un quiz interactivo basado en un deck de flashcards.
    
    Args:
        deck: Lista de diccionarios, cada uno representando una flashcard.
              Cada flashcard debe tener las keys: 'pregunta', 'respuesta', 'categoria'
              y opcionalmente 'explicacion'.
    
    Raises:
        QuizError: Si el deck está vacío o las flashcards tienen estructura inválida
        
    Example:
        >>> deck = [
        ...     {
        ...         'pregunta': '¿Cuál es la capital de Francia?',
        ...         'respuesta': 'París',
        ...         'categoria': 'Geografía',
        ...         'explicacion': 'París es la ciudad más poblada de Francia.'
        ...     }
        ... ]
        >>> iniciar_quiz(deck)
    """
    try:
        # Validación inicial
        if not deck:
            raise QuizError("El deck de flashcards está vacío")
        
        if not isinstance(deck, list):
            raise QuizError("El deck debe ser una lista de flashcards")
        
        # Validar cada flashcard
        for i, flashcard in enumerate(deck):
            if not isinstance(flashcard, dict):
                raise QuizError(f"Flashcard #{i + 1} debe ser un diccionario")
            validar_flashcard(flashcard, i)
        
        # Mezclar el deck para randomizar el orden
        deck_mezclado = deck.copy()
        random.shuffle(deck_mezclado)
        
        # Inicializar variables de seguimiento
        puntuacion_total = 0.0
        correctas_primer_intento = 0
        correctas_segundo_intento = 0
        total_preguntas = len(deck_mezclado)
        
        # Mensaje de bienvenida
        print("🎓 ¡BIENVENIDO AL QUIZ INTERACTIVO!")
        print(f"📝 Tienes {total_preguntas} preguntas por responder.")
        print("💡 Recuerda: tienes 2 intentos por pregunta.")
        print("🏆 Puntuación: 1 punto (1er intento), 0.5 puntos (2do intento)")
        
        # Ejecutar el quiz
        for i, flashcard in enumerate(deck_mezclado, 1):
            try:
                puntos, fue_correcta = ejecutar_pregunta(flashcard, i)
                puntuacion_total += puntos
                
                # Actualizar contadores
                if fue_correcta and puntos == 1.0:
                    correctas_primer_intento += 1
                elif fue_correcta and puntos == 0.5:
                    correctas_segundo_intento += 1
                
            except KeyboardInterrupt:
                print("\n\n⏸️  Quiz interrumpido por el usuario.")
                print("👋 ¡Hasta la próxima!")
                return
            except Exception as e:
                print(f"\n⚠️  Error procesando pregunta {i}: {e}")
                continue
        
        # Mostrar resumen final
        mostrar_resumen_final(puntuacion_total, total_preguntas, 
                            correctas_primer_intento, correctas_segundo_intento)
        
    except QuizError as e:
        print(f"❌ Error en el quiz: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")


if __name__ == "__main__":
    # Ejemplo de uso y testing
    deck_ejemplo = [
        {
            'pregunta': '¿Cuál es la capital de Francia?',
            'respuesta': 'París',
            'categoria': 'Geografía',
            'explicacion': 'París es la ciudad más grande y capital de Francia desde el siglo XII.'
        },
        {
            'pregunta': '¿En qué año llegó el hombre a la Luna?',
            'respuesta': '1969',
            'categoria': 'Historia',
            'explicacion': 'Neil Armstrong fue el primer humano en caminar sobre la Luna el 20 de julio de 1969.'
        },
        {
            'pregunta': '¿Cuál es la fórmula química del agua?',
            'respuesta': 'H2O',
            'categoria': 'Química'
        }
    ]
    
    print("🧪 Ejecutando quiz de ejemplo...")
    iniciar_quiz(deck_ejemplo)