#coding:utf-8
import unittest
from pelicula import Pelicula
from buscador_peliculas import BuscadorPeliculas

class RepositorioMockPeliculas(object):
	def obtener_peliculas(self):
		""" Devuelve un diccionario conteniendo como clave nombres de peliculas
			y como valor los objetos Pelicula correspondientes.
		"""
		return {
			'Inception' : Pelicula('Inception', None, 'Christopher Nolan', None, None),
			'Into the Wild' : Pelicula('Into the Wild', None, 'Sean Penn', None, None),
			'Juno' : Pelicula('Juno', None, 'Jason Reitman', None, None),
			'Rocky' : Pelicula('Rocky', None, 'John G. Avildsen', None, None)
		}

class TestBuscadorPeliculas(unittest.TestCase):
	""" Clase que agrupa los tests unitarios de la clase BuscadorPeliculas. """
	def test_obtener_peliculas_titulo_comienza_In_contiene_Inception(self):
		expected = 'Inception'
		repo = RepositorioMockPeliculas()
		buscador = BuscadorPeliculas(repo)
		actual = buscador.obtener_peliculas_titulo_comienza('In')
		self.assertIn(expected, (peli.titulo for peli in actual))
		
	def test_obtener_peliculas_titulo_comienza_asdasd_retorna_lista_vacia(self):
		expected = []
		repo = RepositorioMockPeliculas()
		buscador = BuscadorPeliculas(repo)
		actual = buscador.obtener_peliculas_titulo_comienza('asdasd')
		self.assertEqual(expected, actual)
		
	def test_obtener_peliculas_titulo_termina_tion_contiene_Inception(self):
		expected = 'Inception'
		repo = RepositorioMockPeliculas()
		buscador = BuscadorPeliculas(repo)
		actual = buscador.obtener_peliculas_titulo_termina('tion')
		self.assertIn(expected, (peli.titulo for peli in actual))
		
	def test_obtener_peliculas_titulo_termina_asdasd_retorna_lista_vacia(self):
		expected = []
		repo = RepositorioMockPeliculas()
		buscador = BuscadorPeliculas(repo)
		actual = buscador.obtener_peliculas_titulo_termina('asdasd')
		self.assertEqual(expected, actual)
		
	def test_obtener_peliculas_titulo_contiene_cepti_contiene_Inception(self):
		expected = 'Inception'
		repo = RepositorioMockPeliculas()
		buscador = BuscadorPeliculas(repo)
		actual = buscador.obtener_peliculas_titulo_contiene('cepti')
		self.assertIn(expected, (peli.titulo for peli in actual))
		
	def test_obtener_peliculas_titulo_contiene_asdasd_retorna_lista_vacia(self):
		expected = []
		repo = RepositorioMockPeliculas()
		buscador = BuscadorPeliculas(repo)
		actual = buscador.obtener_peliculas_titulo_contiene('asdasd')
		self.assertEqual(expected, actual)
		
		
	def test_obtener_peliculas_director_comienza_Christoph_contiene_Inception(self):
		expected = 'Inception'
		repo = RepositorioMockPeliculas()
		buscador = BuscadorPeliculas(repo)
		actual = buscador.obtener_peliculas_director_comienza('Christoph')
		self.assertIn(expected, (peli.titulo for peli in actual))
		
	def test_obtener_peliculas_director_comienza_asdasd_retorna_lista_vacia(self):
		expected = []
		repo = RepositorioMockPeliculas()
		buscador = BuscadorPeliculas(repo)
		actual = buscador.obtener_peliculas_director_comienza('asdasd')
		self.assertEqual(expected, actual)
		
	def test_obtener_peliculas_director_termina_lan_contiene_Inception(self):
		expected = 'Inception'
		repo = RepositorioMockPeliculas()
		buscador = BuscadorPeliculas(repo)
		actual = buscador.obtener_peliculas_director_termina('lan')
		self.assertIn(expected, (peli.titulo for peli in actual))
		
	def test_obtener_peliculas_director_termina_asdasd_retorna_lista_vacia(self):
		expected = []
		repo = RepositorioMockPeliculas()
		buscador = BuscadorPeliculas(repo)
		actual = buscador.obtener_peliculas_director_termina('asdasd')
		self.assertEqual(expected, actual)
		
	def test_obtener_peliculas_director_contiene_pher_Nol_contiene_Inception(self):
		expected = 'Inception'
		repo = RepositorioMockPeliculas()
		buscador = BuscadorPeliculas(repo)
		actual = buscador.obtener_peliculas_director_contiene('pher Nol')
		self.assertIn(expected, (peli.titulo for peli in actual))
		
	def test_obtener_peliculas_director_contiene_asdasd_retorna_lista_vacia(self):
		expected = []
		repo = RepositorioMockPeliculas()
		buscador = BuscadorPeliculas(repo)
		actual = buscador.obtener_peliculas_director_contiene('asdasd')
		self.assertEqual(expected, actual)

def run_tests():
    """Método para iniciar la sesión de testeo"""
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBuscadorPeliculas)
    unittest.TextTestRunner(verbosity=2).run(suite)

#corremos los tests sólo si fuimos llamados desde la consola
if __name__ == "__main__":
    run_tests()