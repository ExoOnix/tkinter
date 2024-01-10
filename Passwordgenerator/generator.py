import random

password = []

def generate_password():
	global password
	lowercase = False
	numbers = False
	Checkbutton = False
	if lowercase == True:
		for i in range(1, 4):
			lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
			lowera = choice(lower)
			lowera.append(password)
			random.shuffle(password)
	if numbers == True:
		for i in range(1, 4):
			num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
			numa = choice(num)
			numa.append(password)
			random.shuffle(password)