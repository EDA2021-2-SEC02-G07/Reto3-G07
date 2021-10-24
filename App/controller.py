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

def loadSightings(Index):
    """
    Carga los avistamientos del archivo. 
    """
    SightingsFile = cf.data_dir + 'UFOS-utf8-30pct.csv'
    input_file = csv.DictReader(open(SightingsFile, encoding='utf-8'))
    j = 0
    for sighting in input_file:
        j += 1
        model.addSighting_to_cities(Index, sighting)
    created_cities = model.mp.size(Index['Cities'])
    keys = model.mp.keySet(Index['Cities'])
    maps_info = [['Ciudad', 'Cantidad de elementos', 'Altura']]
    size = model.lt.size(keys)
    for i in range(1, size + 1): 
        key = model.lt.getElement(keys, i)
        mp = model.me.getValue(model.mp.get(Index['Cities'], key))
        elements = model.om.size(mp)
        height = model.om.height(mp)
        if elements >= 70:
            maps_info.append([key, elements, height])
    

    print('Avistamientos cargados: ', j)
    print('Arboles creados para el requerimiento 1: ', created_cities)
    print('Algunos de los arboles creados por ciudad junto con su información se listan a continuación: ')
    print(tabulate(maps_info, headers='firstrow', tablefmt='fancy_grid', stralign="left"))


    
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
