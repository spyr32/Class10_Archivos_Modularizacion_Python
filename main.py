# Proyecto: Compras Fruteria
# Estudiante: Andrés Mena Abarca
# Fecha de Inicio: 2024/11/13
# Fecha de Entrega: 2024/11/13
# Descripción: Controlar las compras de frutas y verduras
# Version: 0.0

#Importa modulo individual
#from analisis_datos.carga_datos import generar_lista_compras , guardar_lista_compras

#Importar un paquete de modulos
from analisis_datos import *

#Generar una lista de compras aleatoria y escribir esta lista en un archivo
lista_compras = generar_lista_compras()
guardar_lista_compras(lista_compras)
precios = [precio for _, precio in lista_compras]
media = media(precios)
mediana = mediana(precios)
print(f"Media de precios: ¢{media:.2f}")
print(f"Mediana de precios: ¢{mediana:.2f}")