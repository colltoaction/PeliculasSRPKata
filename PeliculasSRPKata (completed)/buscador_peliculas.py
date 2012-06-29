#coding:utf-8
class BuscadorPeliculas(object):
	def __init__(self, peliculas_repo):
		""" Recibe un parámetro peliculas_repo que contiene un método
			obtener_peliculas, que devuelve un diccionario de peliculas.
		"""
		self._peliculas = peliculas_repo.obtener_peliculas()
		
		
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