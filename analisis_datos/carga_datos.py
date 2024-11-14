import random

def generar_lista_compras():
    productos = {
    "Manzana": 250,
    "Banano": 150,
    "Naranja": 200,
    "Pera": 300,
    "Uva": 400,
    "Lechuga": 1000,
    "Tomate": 800,
    "Cebolla": 500,
    "Pan": 350,
    "Huevos (docena)": 1200,
    "Carne de res": 1500,
    "Pollo": 1200,
    "Pescado": 2000,
    "Arroz": 800,
    "Frijoles": 600,
    "Leche": 1000,
    "Queso": 1200,
    "Yogurt": 800,
    "Café": 1000,
    "Té": 500,
    "Azúcar": 300,
    "Aceite": 1500,
    "Harina": 400
    }
    seleccion = random.sample(list(productos.items()),k=5) # K Selecciona la cantidad de productos aleatorios que retorna la lista  
    return seleccion


def guardar_lista_compras(lista_compras, nombre_archivo="lista_compras.txt"):
    try:
        # Operaciones con el archivo
        with open(nombre_archivo, 'w') as archivo:
            for producto, precio in lista_compras:
                archivo.write(f"{producto}:{precio}\n")
        print(f"Lista de compras guardada en '{nombre_archivo}'.")
    except Exception as e:  # Captura cualquier excepción
        print(f"Error al trabajar con el archivo: {e}")
    finally:
        if archivo:
            archivo.close()