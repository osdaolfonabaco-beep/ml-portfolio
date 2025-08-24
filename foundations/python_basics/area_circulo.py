
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
    area = math.pi * (radio ** 2)
    return area

def main():
    """
    Función principal que maneja la interacción con el usuario.
    """
    try:
        user_input = input("Ingrese el radio del círculo: ")
        radio = float(user_input)
        area = calcular_area_circulo(radio)
        print(f"El área del círculo con radio {radio} es: {round(area, 2)}")
    except ValueError as e:
        print(f"Error: {e}. Ingrese un número válido.")

if __name__ == "__main__":
    main()