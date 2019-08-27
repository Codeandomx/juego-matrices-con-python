#!/usr/bin/env python
import os
import random


class Utils():
	@staticmethod
	def cls():
		"""
		Limpia la pantalla de la consola
		"""
		# clear = lambda: os.system('cls') # For windows
		clear = lambda: os.system('clear') # For Linux

		clear()


	@staticmethod
	def getnumber(text):
		"""
		Lee solo numeros enteros
		"""
		# Leemos desde consola
		number = input(text)

		#validamos que sea un numero
		try:
   			val = int(number)
   			return val
		except:
   			return Utils.getnumber(text)


	@staticmethod
	def getrandom(n):
		"""
		Generamos un numero random
		"""
		return random.randint(0, n)