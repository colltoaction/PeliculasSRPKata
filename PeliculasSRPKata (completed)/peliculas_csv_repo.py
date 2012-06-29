#coding:utf-8
import csv
from pelicula import Pelicula

class RepositorioCSVPeliculas(object):
	def __init__(self, path):
		""" Recibe un parámetro path que indica la ubicación del
			archivo csv que contiene las películas.
		"""
		self._path = path
				
	def obtener_peliculas(self):
		""" Devuelve un diccionario conteniendo como clave nombres de peliculas
			y como valor los objetos Pelicula correspondientes.
		"""
		diccionario = {}
		with open(self._path) as archivo:
			reader = csv.reader(archivo, delimiter= ";")
			
			for line in reader:
				diccionario[line[0]] = Pelicula(line[0],
												 int(line[1]),
												 line[2],
												 line[3].split(','),
												 line[4])
		return diccionario