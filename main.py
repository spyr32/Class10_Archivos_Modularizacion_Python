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

lista_compras = generar_lista_compras()
guardar_lista_compras(lista_compras)

precios  = [precio for nombre, precio in lista_compras] #Nombre no se utiliza

print(lista_compras)
print(media(precios))