

import math

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Parámetros:
    radio (float): El radio del círculo. Debe ser un número no negativo.

    Retorna:
    float: El área del círculo.

    Lanza:
    ValueError: Si el radio es negativo.
    """
    if radio < 0:
        raise ValueError("El radio no puede ser negativo")
    return math.pi * (radio ** 2)

def obtener_radio_valido():
    """
    Solicita repetidamente al usuario un radio válido hasta que lo ingrese.

    Retorna:
    float: El radio válido ingresado por el usuario.
    """
    
    intentos_maximos = 3
    intento = 1


    while intento <= intentos_maximos:
        try:
            user_input = input(f"[Intento {intento}/{intentos_maximos}] Ingrese el radio del círculo: ")
            radio = float(user_input)
            
            return calcular_area_circulo(radio) 
        except ValueError as e:
            # Este 'except' captura tanto el error de conversion a float como el que lanza nuestra función.
            print(f"Error: {e}. Por favor, ingrese un número válido.")
            intento += 1 

    
    print("\n❌ Se agotaron los intentos. Cerrando el programa.")
    return None

def main():
    """
    Función principal que maneja la interacción con el usuario.
    """
    area = obtener_radio_valido()

    
    if area is not None:
        print(f"\n✅ El área del círculo es: {area:.2f}")

if __name__ == "__main__":
    main()