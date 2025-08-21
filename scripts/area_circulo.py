
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

if __name__ == "__main__":
    radio = float(input("Ingresa el radio del círculo: "))

    area = calcular_area_circulo(radio)
    print(f"El área del círculo con radio {radio} es: {round(area, 2)}")