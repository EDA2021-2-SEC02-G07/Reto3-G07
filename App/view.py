"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from tabulate import tabulate
import sys
import time
from datetime import datetime
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import orderedmap as om
default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print()
    print('Requerimientos lab 8')
    print("0- Cargar los datos de los avistamientos")
    print("3- Dar altura y número de elementos del árbol de una ciudad")
    print()
    print("1- Contar los avistamientos en una ciudad")
    print("2- Contar los avistamientos por duración")
    print("3- Contar avistamientos por Hora/minutos del día")
    print("4- Contar los avistamientos en un rango de fechas")
    print("5- Contar los avistamientos de una zona geográfica")
    print("6- Visualizar los avistamientos de una zona geográfica")

def initIndex():
    """
    Inicializa el índice de avistamientos
    """
    return controller.initIndex()

def loadData(Index):
    """
    Carga los avistamientos en el índice
    """
    controller.loadSightings(Index)




"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 0:
        print("Cargando información de los archivos ....")
        start_time = time.process_time()
        index = initIndex()
        loadData(index)

        stop_time = time.process_time()
        print()
        print('NOTA: ')
        print('Para este requerimiento decidimos implementar una tabla de hash con keys un ciudad y con árboles de avistamientos como values.')
        print('Por tanto la opción 3 de preguntar por el número de elementos y altura en este lab pide como parametro una ciudad')
        print()
        elapsed_time_mseg = (stop_time - start_time)
        print('La carga demoró', elapsed_time_mseg, 'segundos')

    elif int(inputs[0]) == 1:
        pass

    elif int(inputs[0]) == 2:
        pass

    elif int(inputs[0]) == 3:
        try:
            ciudad = input('Ingrese el nombre de una ciudad a consultar:\n')
            arbol = me.getValue(mp.get(index['Cities'], ciudad))
            elements = om.size(arbol)
            height = om.height(arbol) + 1
            print()
            print('El número de elementos del árbol de avistamientos en la ciudad ' + ciudad + ' es de', elements )
            print()
            print('La altura del árbol de avistamientos en la ciudad ' + ciudad + ' es de', height )
        except:
            print()
            print('ERROR: Por favor ingrese un nombre de ciudad válido.')
    elif int(inputs[0]) == 4:
        pass
    
    elif int(inputs[0]) == 5:
        pass

    elif int(inputs[0]) == 6:
        pass
    
    else:
        sys.exit(0)
sys.exit(0)
