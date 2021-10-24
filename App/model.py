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
    Index = { 'Cities': None
               }
    Index['Cities'] = mp.newMap(700, maptype = 'Probing', loadfactor = 0.5, comparefunction = cmpValueWithEntry)

    
    return Index

# Funciones para agregar informacion al índice

def addSighting_to_cities(Index, sighting_info):
    '''
    Agrega un avistamiento al índice por ciudades organizado por fechas.
    Los argumentos son el índice total (diccionario) y la información 
    del avistamiento (diccionario).
    '''
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
        




# Funciones para creacion de datos
def newCity():
    """
    Se crea una nueva ciudad en el índice de ciudades. En el índice 
    cada ciudad es un arbol binario organizado por fecha de los 
    avistamientos
    """
    city = om.newMap(omaptype='RBT', comparefunction=compareDates)
    return city

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
    latitude = sighting_info['latitude']
    longitude = sighting_info['longitude']

    #En este espacio se pueden limpiar los datos

    sighting['datetime'] = datetime
    sighting['city'] = city
    sighting['country'] = country
    sighting['shape'] = shape
    sighting['duration'] = duration
    sighting['latitude'] = latitude
    sighting['longitude'] = longitude

    return sighting

# Funciones de consulta

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

# Funciones de ordenamiento
