"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import orderedmap as om
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
import time
from datetime import datetime

"""
Se define la estructura de un índice de avistamientos. En este caso el índice tendrá varios maps
dependiendo de las necesidades de consulta.
"""

# Construccion de modelos
def newIndex():
    """
    Inicializa el índice de avistamientos. Crea los maps que se van a usar en cada consulta.
    """
    Index = {  'Cities': None,
               'Coordinates': None,
               'Time': None,
               }
    Index['Cities'] = mp.newMap(700, maptype = 'Probing', loadfactor = 0.5, comparefunction = cmpValueWithEntry)
    Index['Latitudes'] = om.newMap(omaptype='RBT', comparefunction = cmpValues)
    Index['Time'] = om.newMap(omaptype= 'RBT', comparefunction= cmpValues)
    
    return Index

# Funciones para agregar informacion al índice

def addSighting_to_cities(Index, sighting_info):
    """
    Agrega un avistamiento al índice por ciudades organizado por fechas.
    Los argumentos son el índice total (diccionario) y la información 
    del avistamiento (diccionario).
    """
    sighting = newSighting(sighting_info)
    sighting_city = sighting['city']
    sighting_datetime = sighting['datetime']
    cities = Index['Cities']
    if mp.contains(cities, sighting_city):
        city = me.getValue(mp.get(cities, sighting_city))
        om.put(city, sighting_datetime, sighting)

    else: 
        city = newCity()
        mp.put(cities, sighting_city, city)
        om.put(city, sighting_datetime, sighting)


def addSighting_to_times(Index, sighting_info):
    """
    Agrega un avistamiento en el índice por hora del día. 
    Los argumentos son el índice total y la información del
    avistamiento
    """
    sighting = newSighting3(sighting_info)
    sighting_date = sighting['date']
    sighting_time = sighting['time']
    time = Index['Time']
    if om.contains(time, sighting_time):
        hour = me.getValue(om.get(time, sighting_time))
        om.put(hour, sighting_date, sighting)
    else: 
        hour = om.newMap(omaptype= 'RBT', comparefunction= cmpValues)
        om.put(hour, sighting_date, sighting)
        om.put(time, sighting_time, hour)



def addSighting_to_coordinates(Index, sighting_info):
    """
    Agrega un avistamiento el índice de coordenadas. 
    Los argumentos son índice total (diccionario) y la información 
    del avistamiento (diccionario).
    """
    sighting = newSighting2(sighting_info)
    sighting_latitude = sighting['latitude']
    sighting_longitude = sighting['longitude']
    latitudes = Index['Latitudes']
    try:
        longitudes = om.get(latitudes, sighting_latitude)
        om.put(longitudes, sighting_longitude, sighting)
    except:
        longitudes = newCoordinate()
        om.put(longitudes, sighting_longitude, sighting)
        om.put(latitudes, sighting_latitude, longitudes)
        


# Funciones para creacion de datos

def newCity():
    """
    Se crea una nueva ciudad en el índice de ciudades. En el índice 
    cada ciudad es un arbol organizado por fecha de los 
    avistamientos
    """
    city = om.newMap(omaptype = 'RBT', comparefunction = compareDates)
    return city

def newCoordinate():
    """
    Crea una nueva latitud en el índice de coordenadas. Cada latitud es un arbol
    que contiene árboles de longitudes
    """
    coordinate = om.newMap(omaptype = 'RBT', comparefunction = cmpValues)
    return coordinate

def newSighting(sighting_info):
    """
    Crea un diccionario con la información del avistamiento. 
    Como parámetro se recibe un diccionario con la info del
    avistamiento (sighting_info)
    """

    sighting = {'datetime': None,
                'city': None,
                'country': None, 
                'shape': None, 
                'duration': None
               }
    datetime = sighting_info['datetime']
    city = sighting_info['city']
    country = sighting_info['country']
    shape = sighting_info['shape']
    duration = sighting_info['duration (seconds)']

    #En este espacio se pueden limpiar los datos

    sighting['datetime'] = datetime
    sighting['city'] = city
    sighting['country'] = country
    sighting['shape'] = shape
    sighting['duration'] = duration

    return sighting


def newSighting2(sighting_info):
    """
    Crea un diccionario con la información del avistamiento. 
    Como parámetro se recibe un diccionario con la info del
    avistamiento (sighting_info)
    """

    sighting = {'datetime': None,
                'city': None,
                'country': None, 
                'shape': None, 
                'duration': None,
                'latitude': None,
                'longitude': None
               }
    datetime = sighting_info['datetime']
    city = sighting_info['city']
    country = sighting_info['country']
    shape = sighting_info['shape']
    duration = sighting_info['duration (seconds)']
    latitude = round(float(sighting_info['latitude']), 2)
    longitude = round(float(sighting_info['longitude']), 2)



    sighting['datetime'] = datetime
    sighting['city'] = city
    sighting['country'] = country
    sighting['shape'] = shape
    sighting['duration'] = duration
    sighting['latitude'] = latitude
    sighting['longitude'] = longitude

    return sighting

def newSighting3(sighting_info):
    """
    Crea un diccionario con la información del avistamiento. 
    Como parámetro se recibe un diccionario con la info del
    avistamiento (sighting_info)
    """

    sighting = {'date': None,
                'time': None,
                'city': None,
                'country': None, 
                'shape': None, 
                'duration': None,
                'latitude': None,
                'longitude': None
               }
    datetime = sighting_info['datetime']
    city = sighting_info['city']
    country = sighting_info['country']
    shape = sighting_info['shape']
    duration = sighting_info['duration (seconds)']
    latitude = round(float(sighting_info['latitude']), 2)
    longitude = round(float(sighting_info['longitude']), 2)



    sighting['date'] = datetime[0:10]
    sighting['time'] = datetime[11:]
    sighting['city'] = city
    sighting['country'] = country
    sighting['shape'] = shape
    sighting['duration'] = duration
    sighting['latitude'] = latitude
    sighting['longitude'] = longitude

    return sighting

    #En este espacio se pueden limpiar los datos

# Funciones de consulta



def sightings_in_city(Index, cityname):
    """
    Retorna una tupla con una lista que contiene los primeros 3 y últimos 3 avistamientos reportados en
    una ciudad ordenados cronológicamente. Las entradas son el índice y el nombre de la ciudad
    """
    city_sightings = me.getValue(mp.get(Index['Cities'], cityname))
    keys = om.keySet(city_sightings)
    size = lt.size(keys)
    sightings = []
    sightingsb = []
    if size >= 6:
        for i in range(1, 4):
            key = lt.getElement(keys, i)
            sighting = me.getValue(om.get(city_sightings, key))
            sightings.append(sighting)
        for i in range(size - 2, size + 1):
            key = lt.getElement(keys, i)
            sighting = me.getValue(om.get(city_sightings, key))
            sightings.append(sighting)
    else: 
        for i in range(1, size + 1):
            key = lt.getElement(keys, i)
            sighting = me.getValue(om.get(city_sightings, key))
            sightings.append(sighting)
            
    return sightings, size

        

def sightings_in_time(Index, timelo, timehi):
    
    times = Index['Time']
    times_list = om.values(times, timelo, timehi)
    list_size = lt.size(times_list)
    sightings = []
    count = 0
    x = 0
    for i in range(1, list_size + 1):
        dates = lt.getElement(times_list, i)
        keys = om.keySet(dates)
        keys_size = lt.size(keys)
        count += keys_size
        for j in range(1, keys_size + 1):
            if x >= 6: 
                break
            key = lt.getElement(keys, j)
            sighting = me.getValue(om.get(dates, key))
            sightings.append(sighting)
            x += 1
    if count  <= 6: 
        return sightings, count
    else: 
        sightings = sightings[0:3]
        n = 0
        sightingsb = []
        for k in range(1, list_size + 1):
            i = list_size + 1 - k
            dates = lt.getElement(times_list, i)
            keys = om.keySet(dates)
            keys_size = lt.size(keys)       
            for k in range(1, keys_size + 1):
                j = keys_size + 1 - k
                if n >= 3: 
                    break
                key = lt.getElement(keys, j)
                sighting = me.getValue(om.get(dates, key))
                sightingsb.append(sighting) 
                n += 1
        for l in range(0, 3):
            sightings.append(sightingsb[len(sightingsb) - 1 - l])
    return sightings, count

def latest_sightings(Index): 
    Times = Index['Time']
    last_time = om.maxKey(Times)
    latest_sighting_map = me.getValue(om.get(Times, last_time))
    count = om.size(latest_sighting_map)

    return(last_time, count)


def sightings_in_coordinates(Index, latitudelo, latitudehi, longitudelo, longitudehi, req):
    """
    Retorna una tupla que contiene una lista con los avistamientos en unas coordenadas específicas
    y la cantidad de avistamientos en las coordenadas ingresadas.
    Las entradas son el índice Index, las coordenadas como floats y el número del req (5 o 6)
    Dependiendo de si el req ingresado es 5 o 6, la lista retornada contiene todos los 
    avistamientos en el rango o los 5 primeros y 5 últimos
    """
    latitudes = Index['Latitudes']
    latitudes_list = om.values(latitudes, latitudelo, latitudehi)
    list_size = lt.size(latitudes_list)

    counter = 0
    sightings = []
    n = 0
    if req == 6:
        for i in range(1, list_size + 1):
            longitudes = lt.getElement(latitudes_list, i)
            longitudes_list = om.values(longitudes, longitudelo, longitudehi)
            longitudes_size = lt.size(longitudes_list)
            counter += longitudes_size
            for j in range(1, longitudes_size + 1):
                sighting = lt.getElement(longitudes_list, j)
                sightings.append(sighting)
    elif req == 5:
        for i in range(1, list_size + 1):
            longitudes = lt.getElement(latitudes_list, i)
            longitudes_list = om.values(longitudes, longitudelo, longitudehi)
            longitudes_size = lt.size(longitudes_list)
            counter += longitudes_size
            for j in range(1, longitudes_size + 1):
                if n >= 10: 
                    break
                sighting = lt.getElement(longitudes_list, j)
                sightings.append(sighting)
                n += 1

        if counter <= 10:
            return sightings, counter
        else: 
            sightings = sightings[0:5]

        x = 0
        sightingsb = []
        for i in range(0, list_size):
            if x >= 5:
                break
            pos = list_size - i
            longitudes = lt.getElement(latitudes_list, pos)
            longitudes_list = om.values(longitudes, longitudelo, longitudehi)
            longitudes_size = lt.size(longitudes_list)
            for j in range(0, longitudes_size):
                if x >= 5: 
                    break
                pos = longitudes_size - j
                sighting = lt.getElement(longitudes_list, pos)
                sightingsb.append(sighting)
                x += 1
        for i in range(0, 5):
            sightings.append(sightingsb[len(sightingsb)-i-1])
    return sightings, counter



# Funciones de comparación

def cmpValueWithEntry(value, entry):
    """
    Compara una llave de entrada (value) con la llave de la pareja llave
    valor de un map (entry).
    """
    keyentry = me.getKey(entry)
    if value == keyentry:
        return 0
    elif value > keyentry:
        return 1
    else:
        return -1

def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def cmpValues(value1, value2):
    """
    Compara dos valores numéricos o str cualquiera
    """
    if value1 == value2:
        return 0
    elif value1 > value2:
        return 1
    else: 
        return -1

# Funciones de ordenamiento
