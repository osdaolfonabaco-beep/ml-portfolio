#!/usr/bin/env python3
"""
Script de prueba para el módulo quizme.py.
Simula un deck de flashcards y prueba la función iniciar_quiz.
"""

# Importamos la función que vamos a probar
from quizme import iniciar_quiz

# Creamos un deck de ejemplo para las pruebas
deck_ejemplo = [
    {
        "pregunta": "¿Qué significa API?",
        "respuesta": "Application Programming Interface",
        "explicacion": "Es un conjunto de reglas que permite a diferentes aplicaciones comunicarse entre sí.",
        "categoria": "Conceptos Generales"
    },
    {
        "pregunta": "¿Qué hace el método .get() en un diccionario Python?",
        "respuesta": "Devuelve el valor de una clave si existe, o un valor por defecto si no existe",
        "explicacion": "Es más seguro que usar diccionario[clave] porque evita KeyError.",
        "categoria": "Python"
    },
    {
        "pregunta": "¿Para qué sirve git commit?",
        "respuesta": "Para guardar los cambios en el historial del repositorio",
        "categoria": "Git"  # Esta flashcard NO tiene "explicacion"
    }
]

def main():
    """Función principal que ejecuta la prueba."""
    print("🧪 INICIANDO PRUEBA DEL SISTEMA DE QUIZ")
    print("=" * 50)
    
    # Ejecutamos el quiz con nuestro deck de ejemplo
    iniciar_quiz(deck_ejemplo)
    
    print("=" * 50)
    print("✅ Prueba completada. Revisa si el comportamiento fue el esperado.")

if __name__ == "__main__":
    main()