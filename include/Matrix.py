#!/usr/bin/env python
from include.Utils import Utils


class Matrix:
	def __init__(self):
		"""
		constructor
		"""
		# Obtenemos filas y columnas
		self.rows = Utils.getnumber("Ingresa numero de filas: ")
		self.cols = Utils.getnumber("Ingresa numero de columnas: ")

		# Creamos la matriz
		self.m = [[0 for x in range(self.cols)] for y in range(self.rows)]

		# Llenamos la matriz
		for i in range(0, self.rows):
			for j in range(0, self.cols):
				self.m[i][j] = 0

		# Obtenemos la posicion del cursor
		self.pos_r = Utils.getrandom(self.rows - 1)
		self.pos_c = Utils.getrandom(self.cols - 1)


	def print(self):
		"""
		Imprimimos una matriz
		"""
		# Limpiamos la pantalla
		Utils.cls()
		
		# Imprimimos la matriz
		# [print(*line) for line in self.m]
		for i in range(self.rows):
			for j in range(self.cols):
				#validamos si se encuentra en la posicion del cursor
				if self.pos_r == i and self.pos_c == j:
					print("%4s" % ("*"+str(self.m[i][j])), end="")
				else:
					print("%4d" % (self.m[i][j]), end="")
			print('\n')


	def left(self):
		"""
		Recorremos el cursor a la izquierda
		"""
		# Validamos si esta en el limite
		if self.pos_c == 0:
			# Asignamos nuevo valor
			self.pos_c = self.cols - 1
		else:
			self.pos_c -= 1


	def right(self):
		"""
		Recorremos el cursor a la derecha
		"""
		# Validamos si esta en el limite
		if self.pos_c == self.cols - 1:
			# Asignamos nuevo valor
			self.pos_c = 0
		else:
			self.pos_c += 1


	def up(self):
		"""
		Recorremos el cursor hacia arriba
		"""
		# Validamos si esta en el limite
		if self.pos_r == 0:
			# Asignamos nuevo valor
			self.pos_r = self.rows - 1
		else:
			self.pos_r -= 1	


	def down(self):
		"""
		Recorremos el cursor hacia abajo
		"""
		# Validamos si esta en el limite
		if self.pos_r == self.rows - 1:
			# Asignamos nuevo valor
			self.pos_r = 0
		else:
			self.pos_r += 1


	def move(self):
		"""
		Incrementamos el valor de los vecinos
		"""
		top = 0
		bottom = 0
		left = 0
		right = 0

		# Validamos el limite superior
		if self.pos_r == 0:
			top = self.rows - 1
		else:
			top = self.pos_r - 1

		# Validamos el limite inferior
		if self.pos_r == self.rows - 1:
			bottom = 0
		else:
			bottom = self.pos_r + 1

		# Validamos limite izquierdo
		if self.pos_c == 0:
			left = self.cols - 1
		else:
			left = self.pos_c - 1

		# Validamos limite derecho
		if self.pos_c == self.cols - 1:
			right = 0
		else:
			right = self.pos_c + 1

		# Incrementamos la celda central
		if self.m[self.pos_r][self.pos_c] == 9:
			self.m[self.pos_r][self.pos_c] = 0
		else:
			self.m[self.pos_r][self.pos_c] += 1

		# Incrementamos los vecinos iszquierdos
		if self.m[self.pos_r][left] == 9:
			self.m[self.pos_r][left] = 0
		else:
			self.m[self.pos_r][left] += 1

		# Incrementamos los vecinos derechos
		if self.m[self.pos_r][right] == 9:
			self.m[self.pos_r][right] = 0
		else:
			self.m[self.pos_r][right] += 1

		# incrementamos los vecinos top y bottom
		for i in range(0, 3):
			# Vecinos top
			if self.m[top][left] == 9:
				self.m[top][left] = 0
			else:
				self.m[top][left] += 1

			# Vecinos bottom
			if self.m[bottom][left] == 9:
				self.m[bottom][left] = 0
			else:
				self.m[bottom][left] += 1

			if left == self.cols - 1:
				left = 0
			else:
				left += 1
		

		# Imprimimos la matriz
		self.print()