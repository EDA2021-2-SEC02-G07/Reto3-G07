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
 """

import config as cf
import model
import csv
from tabulate import tabulate

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def initIndex():
    """
    Llama la función de iniciación de creación del índice en el modelo
    """
    Index = model.newIndex()
    return Index

# Funciones para la carga de datos

def loadSightings(index):
    """
    Carga los avistamientos del archivo. 
    """
    SightingsFile = cf.data_dir + 'UFOS-utf8-small.csv'
    input_file = csv.DictReader(open(SightingsFile, encoding='utf-8'))
    j = 0
    for sighting in input_file:
        j += 1
        model.addSighting_to_cities(index, sighting)
        model.addSighting_to_coordinates(index, sighting)

    size = model.mp.size(index['Cities'])
    
    

    print('Avistamientos cargados: ', j)



    
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def sightings_in_coordinates(Index, latitudelo, latitudehi, longitudelo, longitudehi):
    sightings = model.sightings_in_coordinates(Index, latitudelo, latitudehi, longitudelo, longitudehi)
    lensightings = len(sightings)
    if lensightings <=10:
        return sightings
    else: 

        sightings_lo = sightings[0:6]
        sightings_hi = sightings[lensightings - 5: lensightings]
        sightings_clean = sightings_lo + sightings_hi
        return sightings_clean 
