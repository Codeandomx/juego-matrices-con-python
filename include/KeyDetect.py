"""
Docs: https://pypi.python.org/pypi/keyboard
"""

from curtsies import Input
from include.Matrix import Matrix


class KeyDetect:
	@staticmethod
	def run():
		"""
		Quedamos en escucha de eventos del teclado
		"""

		# Inicializamos la matriz
		m = Matrix()

		# Imprimimos la matriz
		m.print()

		# Detectamos las teclas pulsadas
		try:
			with Input(keynames='curses') as input_generator:
				for e in input_generator:
					if str(e) == "KEY_UP":
						m.up()
						m.move()
					if str(e) == "KEY_DOWN":
						m.down()
						m.move()
					if str(e) == "KEY_LEFT":
						m.left()
						m.move()
					if str(e) == "KEY_RIGHT":
						m.right()
						m.move()
		except:
			print("Programa finalizado..")