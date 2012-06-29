#coding:utf-8
import csv
from pelicula import Pelicula

class BuscadorPeliculas(object):
	def __init__(self):
		self._peliculas = {}
		self._importar_peliculas_csv("../peliculas.csv")
		
		
	def obtener_peliculas_titulo_comienza(self, titulo):
		""" Devuelve una lista de los objetos Pelicula cuyo título comience como
			el parámetro titulo, o una lista vacía si ninguna concuerda.
		"""
		lista = []
		for pelicula in self._peliculas.itervalues():
			if pelicula.titulo.startswith(titulo):
				lista.append(pelicula)
		return lista
		
	def obtener_peliculas_titulo_termina(self, titulo):
		""" Devuelve una lista de los objetos Pelicula cuyo título termine como
			el parámetro titulo, o una lista vacía si ninguna concuerda.
		"""
		lista = []
		for pelicula in self._peliculas.itervalues():
			if pelicula.titulo.endswith(titulo):
				lista.append(pelicula)
		return lista
		
	def obtener_peliculas_titulo_contiene(self, titulo):
		""" Devuelve una lista de los objetos Pelicula cuyo título contenga
			el parámetro titulo, o una lista vacía si ninguna concuerda.
		"""
		lista = []
		for pelicula in self._peliculas.itervalues():
			if titulo in pelicula.titulo:
				lista.append(pelicula)
		return lista
		
		
	def obtener_peliculas_director_comienza(self, director):
		""" Devuelve una lista de los objetos Pelicula cuyo director comience como
			el parámetro director, o una lista vacía si ninguna concuerda.
		"""
		lista = []
		for pelicula in self._peliculas.itervalues():
			if pelicula.director.startswith(director):
				lista.append(pelicula)
		return lista
		
	def obtener_peliculas_director_termina(self, director):
		""" Devuelve una lista de los objetos Pelicula cuyo director termine como
			el parámetro director, o una lista vacía si ninguna concuerda.
		"""
		lista = []
		for pelicula in self._peliculas.itervalues():
			if pelicula.director.endswith(director):
				lista.append(pelicula)
		return lista
		
	def obtener_peliculas_director_contiene(self, director):
		""" Devuelve una lista de los objetos Pelicula cuyo director contenga
			el parámetro director, o una lista vacía si ninguna concuerda.
		"""
		lista = []
		for pelicula in self._peliculas.itervalues():
			if director in pelicula.director:
				lista.append(pelicula)
		return lista
		
		
		

	def _importar_peliculas_csv(self, path):
		""" Recibe un path correspondiente a un archivo csv, con valores delimitados por ;
			e importa todas las películas en dicho archivo.
		"""
		with open(path) as archivo:
			reader = csv.reader(archivo, delimiter= ";")
			
			for line in reader:
				self._agregar_registro(line)

	def _agregar_registro(self, lista):
		""" Añade a la base una pelicula a partir de una lista de valores.
		"""
		self._peliculas[lista[0]] = Pelicula(lista[0], int(lista[1]), lista[2], lista[3].split(','), lista[4])