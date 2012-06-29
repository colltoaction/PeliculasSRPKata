#coding:utf-8
class Pelicula(object):
	def __init__(self, titulo, anio, director, actores, genero):
		""" Inicializa un objeto de la clase Pelicula a partir de 6 parametros.
			Estos son asignados a las propiedades de la pelicula.
		"""
		self.titulo = titulo
		self.anio = anio
		self.director = director
		self.actores = actores
		self.genero = genero