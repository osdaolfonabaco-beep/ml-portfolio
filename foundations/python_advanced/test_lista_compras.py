import pytest
import os
import json
from foundations.python_advanced.lista_compras import cargar_lista, guardar_lista, agregar_item, eliminar_item, calcular_total, aplicar_descuento

def test_agregar_item_valido():
    """Test: Agregar item con datos válidos."""
    lista = []
    agregar_item(lista, "Manzana", 1.5, 2)
    assert len(lista) == 1
    assert lista[0]["nombre"] == "Manzana"
    assert lista[0]["precio"] == 1.5
    assert lista[0]["cantidad"] == 2

def test_agregar_item_precio_negativo():
    """Test: Intentar agregar item con precio negativo."""
    lista = []
    with pytest.raises(ValueError, match="El precio no puede ser negativo"):
        agregar_item(lista, "Manzana", -1.5)

def test_agregar_item_cantidad_invalida():
    """Test: Intentar agregar item con cantidad inválida."""
    lista = []
    with pytest.raises(ValueError, match="La cantidad debe ser al menos 1"):
        agregar_item(lista, "Manzana", 1.5, 0)

def test_calcular_total():
    """Test: Cálculo correcto del total."""
    lista = [
        {"nombre": "Manzana", "precio": 1.5, "cantidad": 2},
        {"nombre": "Pan", "precio": 2.0, "cantidad": 1}
    ]
    assert calcular_total(lista) == 5.0

def test_calcular_total_lista_vacia():
    """Test: Cálculo del total con lista vacía."""
    lista = []
    assert calcular_total(lista) == 0.0

def test_eliminar_item_existente():
    """Test: Eliminar item por índice válido."""
    lista = [{"nombre": "Manzana", "precio": 1.5, "cantidad": 2}]
    eliminar_item(lista, 0)
    assert len(lista) == 0

def test_eliminar_item_indice_invalido():
    """Test: Intentar eliminar item con índice inválido."""
    lista = [{"nombre": "Manzana", "precio": 1.5, "cantidad": 2}]
    with pytest.raises(IndexError, match="Índice fuera de rango"):
        eliminar_item(lista, 5)

def test_aplicar_descuento():
    """Test: Aplicar descuento a un item."""
    item = {"nombre": "Manzana", "precio": 100.0, "cantidad": 1}
    aplicar_descuento(item, 20.0)
    assert item["precio"] == 80.0

def test_guardar_y_cargar_lista(tmp_path):
    """Test: Guardar y cargar lista desde archivo."""
    lista_original = [{"nombre": "Test", "precio": 1.0, "cantidad": 1}]
    archivo_test = tmp_path / "test_lista.json"
    
    guardar_lista(lista_original, str(archivo_test))
    lista_cargada = cargar_lista(str(archivo_test))
    
    assert lista_cargada == lista_original

def test_cargar_lista_archivo_inexistente():
    """Test: Cargar lista cuando el archivo no existe."""
    lista = cargar_lista("archivo_que_no_existe.json")
    assert lista == []