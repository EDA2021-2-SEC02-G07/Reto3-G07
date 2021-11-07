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
    print('')
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
        elapsed_time_mseg = (stop_time - start_time)
        print('La carga demoró', elapsed_time_mseg, 'segundos')

    elif int(inputs[0]) == 1:
        try:
            cityname = input('Ingrese el nombre de la ciudad a consultar: ')
            sightings, size = controller.sightings_in_city(index, cityname)
        except:
            print('Por favor ingrese una ciudad válida')
            continue
        table = [['Fecha y hora', 'Ciudad', 'País', 'Forma del objeto', 'Duración (s)']]
        for sighting in sightings:
            datetime = sighting['datetime']
            city = sighting['city']
            country = sighting['country']
            shape = sighting['shape']
            duration = sighting['duration']
            table.append([datetime, city, country, shape, duration])
        print('Hay', size, 'avistamientos dentro de las coordenadas ingresadas')
        print('Los datos de los 3 primeros y 3 últimos avistamientos son:')
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))         



        print('Hay', size, 'avistamientos reportados en', cityname)


    elif int(inputs[0]) == 2:
        pass

    elif int(inputs[0]) == 3:
        
        try:
            timelo = input('Ingrese la hora menor del rango: ')
            timehi = input('Ingrese la hora mayor del rango: ')
            sightings, size = controller.sightings_in_time(index, timelo, timehi)
        except:
            print('Por favor ingrese un rango válido')
            continue
        last_hour, count = controller.latest_sightings(index)


        print('La hora más tardía a la que se han reportado avistamientos es:')
        table = [['Hora', 'Cantidad']]
        table.append([last_hour, count])
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))  
        print('Hay', size, 'avistamientos reportados en el rango')
        table = [['Hora', 'Fecha', 'Ciudad', 'País', 'Forma del objeto', 'Duración (s)']]
        for sighting in sightings:
            time = sighting['time']
            date = sighting['date']
            city = sighting['city']
            country = sighting['country']
            shape = sighting['shape']
            duration = sighting['duration']
            table.append([time, date, city, country, shape, duration])
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))  

    elif int(inputs[0]) == 4:
        pass
    
    elif int(inputs[0]) == 5:
        try:
            coordinates = input('Ingrese las coordenadas en formato "Latitud1, Latitud2, Longitud1, longitud2": ')
            coordinates = coordinates.split(',')
            latitudelo = float(coordinates[0])
            latitudehi = float(coordinates[1])
            longitudelo = float(coordinates[2])
            longitudehi = float(coordinates[3])
            sightings, size = controller.sightings_in_coordinates(index, latitudelo, latitudehi, longitudelo, longitudehi, 5)
        except: 
            print('Por favor ingrese valores de coordenadas válidos')
            continue
        table = [['Fecha y hora', 'Ciudad', 'País', 'Forma del objeto', 'Duración (s)', 'Latitud', 'Longitud']]
        for sighting in sightings:
            datetime = sighting['datetime']
            city = sighting['city']
            country = sighting['country']
            shape = sighting['shape']
            duration = sighting['duration']
            latitude = float(sighting['latitude'])
            longitude = float(sighting['longitude'])
            table.append([datetime, city, country, shape, duration, latitude, longitude])
        print('Hay', size, 'avistamientos dentro de las coordenadas ingresadas')
        print('Los datos de los 5 primeros y 5 últimos avistamientos son:')
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid')) 
        
    elif int(inputs[0]) == 6:
        pass
    
    else:
        sys.exit(0)
sys.exit(0)
