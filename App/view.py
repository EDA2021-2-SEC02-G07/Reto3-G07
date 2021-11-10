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
import folium
import webbrowser
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
    print("0- Cargar los datos de los avistamientos")
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

def Req2print(index, sightings):
    mapa = index['durationsSec']
    n = om.size(mapa)
    m = n - 5
    print('============== Req No.2 Outputs ==============')
    print('Hay',n ,'distintas duraciones de avistamientos')
    start_time = time.process_time()
    totalsightings = om.values(mapa, om.minKey(mapa), om.maxKey(mapa))
    table = [['durations (seconds)', 'count']]
    while n > m:
        mayorSight = lt.getElement(totalsightings, n)
        key = float(lt.getElement(mayorSight, 1)['duration (seconds)'])
        table.append([key, lt.size(mayorSight)])
        n -= 1
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid')) 

    list2 = controller.giveRangeOfDurations(sightings)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)
    print()
    print('Hay', lt.size(list2), 'avistamientos en el rango de duraciones.')
    print('Las primeras y la últimas 3 son:')
    table = [['datetime', 'city', 'country', 'shape', 'durations (seconds)']]
    i = 1
    while i <= 3:
        sg = lt.getElement(list2, i)
        table.append([sg['datetime'], sg['city'], sg['country'], sg['shape'], sg['duration (seconds)']])
        i += 1
    i = lt.size(list2)-2
    while i <= lt.size(list2):
        sg = lt.getElement(list2, i)
        table.append([sg['datetime'], sg['city'], sg['country'], sg['shape'], sg['duration (seconds)']])
        i += 1
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid')) 
    print('La carga demoró', elapsed_time_mseg, 'segundos')

def Req4print(index, sightings):
    mapa = index['Sdates']
    n = 1
    print()
    print('============== Req No.4 Outputs ==============')
    print('Hay',om.size(index['Sdates']) ,'distintas fechas de avistamientos')
    start_time = time.process_time()
    totalsightings = om.values(mapa, om.minKey(mapa), om.maxKey(mapa))
    table = [['durations (seconds)', 'count']]
    while n <= 5:
        mayorSight = lt.getElement(totalsightings, n)
        key = (lt.getElement(mayorSight, 1)['datetime'])
        table.append([key, lt.size(mayorSight)])
        n += 1
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid')) 

    list2 = controller.giveRangeOfDatetimes(sightings)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)
    print()
    print('Hay', lt.size(list2), 'avistamientos en el rango de duraciones.')
    print('Las primeras y la últimas 3 son:')
    table = [['datetime', 'city', 'country', 'shape', 'durations (seconds)']]
    i = 1
    while i <= 3:
        sg = lt.getElement(list2, i)
        table.append([sg['datetime'], sg['city'], sg['country'], sg['shape'], sg['duration (seconds)']])
        i += 1
    i = lt.size(list2)-2
    while i <= lt.size(list2):
        sg = lt.getElement(list2, i)
        table.append([sg['datetime'], sg['city'], sg['country'], sg['shape'], sg['duration (seconds)']])
        i += 1
    print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))  
    print('La carga demoró', elapsed_time_mseg, 'segundos')
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
            start_time = time.process_time()
            sightings, size = controller.sightings_in_city(index, cityname)
            stop_time = time.process_time()
            elapsed_time_mseg = (stop_time - start_time)
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
        print('La carga demoró', elapsed_time_mseg, 'segundos')     

    elif int(inputs[0]) == 2:
        try:
                min = float(input('Ingrese la duración de segundos mínima:\n'))
                max = float(input('Ingrese la duración de segundos máxima:\n'))
                print()
                print('============== Req No.2 Inputs ==============')
                print('Buscando avistamientos entre', min, 'y', max)
                Req2print(index, om.values(index['durationsSec'], min, max))
        except:    
                print()
                print('ERROR: Por favor ingresar parámetros válidos.')

    elif int(inputs[0]) == 3:
        
        try:
            timelo = input('Ingrese la hora menor del rango: ')
            timehi = input('Ingrese la hora mayor del rango: ')
            start_time = time.process_time()
            sightings, size = controller.sightings_in_time(index, timelo, timehi)
        except:
            print('Por favor ingrese un rango válido')
            continue
        last_hour, count = controller.latest_sightings(index)
        stop_time = time.process_time()
        elapsed_time_mseg = (stop_time - start_time)


        print('La hora más tardía a la que se han reportado avistamientos es:')
        table = [['Hora', 'Cantidad']]
        table.append([last_hour, count])
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))  
        print('Hay', size, 'avistamientos reportados en el rango')
        print('Los datos de los 3 primeros y 3 últimos avistamientos son:')
        table = [['Hora', 'Fecha', 'Ciudad', 'País', 'Forma del objeto', 'Duración (s)']]
        for sighting in sightings:
            time1 = sighting['time']
            date = sighting['date']
            city = sighting['city']
            country = sighting['country']
            shape = sighting['shape']
            duration = sighting['duration']
            table.append([time1, date, city, country, shape, duration])
        print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))  
        print('La carga demoró', elapsed_time_mseg, 'segundos') 

    elif int(inputs[0]) == 4:
        try:
            InitialYear = int(input('Escriba el año inicial de las obras (AAAA): '))
            InitialMonth = int(input('Escriba el mes inicial de las obras (MM): '))
            InitialDay = int(input('Escriba el día inicial de las obras (DD): '))
            FinalYear = int(input('Escriba el año final de las obras (AAAA): ')) 
            FinalMonth = int(input('Escriba el mes inicial de las obras (MM): '))
            FinallDay = int(input('Escriba el día inicial de las obras (DD): '))
            beginDate = str(InitialYear) +'-' + str(InitialMonth) +'-' + str(InitialDay) + ' 00:00:00'
            endDate = str(FinalYear) + '-' + str(FinalMonth) + '-' + str(FinallDay) + ' 23:59:59'
            bd = str(InitialYear) +'-' + str(InitialMonth) +'-' + str(InitialDay)
            ed = str(FinalYear) + '-' + str(FinalMonth) + '-' + str(FinallDay) 
            date_object1 = datetime.strptime(beginDate, '%Y-%m-%d %H:%M:%S')
            date_object2 = datetime.strptime(endDate, '%Y-%m-%d %H:%M:%S')
            print()
            print('============== Req No.4 Inputs ==============')
            print('Busca avistamientos entre ', bd, ' y ', ed)
            Req4print(index, om.values(index['Sdates'], beginDate, endDate))
        except:  
            print()
            print('ERROR: Por favor ingresar parámetros válidos.')   
    
    elif int(inputs[0]) == 5:
        try:
            latitudelo = float(input('Ingrese las latitud menor del rango": '))
            latitudehi = float(input('Ingrese las latitud mayor del rango": '))
            longitudelo = float(input('Ingrese las longitud menor del rango": '))
            longitudehi = float(input('Ingrese las longitud mayor del rango": '))
            start_time = time.process_time()
            sightings, size = controller.sightings_in_coordinates(index, latitudelo, latitudehi, longitudelo, longitudehi, 5)
            stop_time = time.process_time()
            elapsed_time_mseg = (stop_time - start_time)
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
        print('La carga demoró', elapsed_time_mseg, 'segundos') 
        
    elif int(inputs[0]) == 6:
        try:
            latitudelo = float(input('Ingrese las latitud menor del rango": '))
            latitudehi = float(input('Ingrese las latitud mayor del rango": '))
            longitudelo = float(input('Ingrese las longitud menor del rango": '))
            longitudehi = float(input('Ingrese las longitud mayor del rango": '))
            sightings, size = controller.sightings_in_coordinates(index, latitudelo, latitudehi, longitudelo, longitudehi, 5)
            mi_mapa = folium.Map(location=(30,-100), zoom_start=4)
            for sighting in sightings:
                latitude = float(sighting['latitude'])
                longitude = float(sighting['longitude'])
                marcador = folium.Marker(location=(latitude, longitude))
                marcador.add_to(mi_mapa)
            
            mi_mapa.save("mapa.html")
            webbrowser.open_new('mapa.html')
        except: 
            print('Por favor ingrese valores de coordenadas válidos')
            continue 
    
    else:
        sys.exit(0)
sys.exit(0)
