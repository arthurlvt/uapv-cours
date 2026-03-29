""" EXERCICE 1: LA FONCTION CARRÉ """

def delta(a, b, c):
	return b**2 - (4*a*c)

def resoudre(a, b, c):
	x1 = 0
	x2 = 0
	x3 = 0
	d = delta(a, b, c)
	if d > 0:
		x1 = (-b - (d**0.5))/(2*a)
		x2 = (-b + (d**0.5))/(2*a)
		return f"Deux solutions: {x1}, {x2}"
	elif d == 0:
		x3 = -b/(2*a)
		return f"Une solution: {x3}"
	else:
		return "aucune solutions"

a = float(input("Entrez a"))
b = float(input("Entrez b"))
c = float(input("Entrez c"))

print(resoudre(a, b ,c))



""" EXERCICE 2: LES NOMBRES PREMIERS """

def est_premier(n):
	if n < 2:
		return False
	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
		i += 1
	return True	

def plus_petit_diviseur(n):
	if n < 2:
		return False
		
	for i in range(2, n + 1):
		if n % i == 0:
			return i

def decomp_facteurs_premiers(n):
	resultat = ""
	d = plus_petit_diviseur(n)
	
	while n > 1:
		resultat += str(d)
		n //= d
		if n > 1:
			resultat += "x"
	return resultat

		
n = int(input("Entrez n: "))
print(f"PLus petit diviseur premier de n : {plus_petit_diviseur(n)}")
print(f"n est-il premier ? {est_premier(n)}")
print(decomp_facteurs_premiers(n))


""" EXERCICE 3: GÉNÉRER UN NOMBRE SECRET ET DEVINER """

import math
import random
import sys
	
def generer_nombre(minimum, maximum):
	return random.randint(minimum, maximum)

def verifier_nombre(secret, proposition):
	if (proposition < secret):
		print("Bravo")
	elif (proposition > secret):
		print("Trop petit")
	else:
		print("Trop grand")
	return False	

def jouer(secret, tentatives):
	while tentatives > 0:
		proposition = int(input("Entrez une proposition: "))
		if verifier_nombre(secret, proposition):
			print("Bien joué!")
			return
		tentatives -= 1
		print(f"Il te reste {tentatives} tentatives")
		print(f"Perdu! Le nombre était {secret}")
def main():
	minimum = int(input("Entrez un minimum: "))
	maximum = int(input("Entrez un maximum: "))
	tentatives = int(input("Entrez un nombre de tentatives: "))
	secret = generer_nombre(minimum, maximum)
	jouer(secret, tentatives)
	if proposition == secret:
		sys.exit()
		
if __name__ == "__main__":
	main()
			
	



""" EXERCICE 4: LES FACTORIELLES """

def factorielle(n):
	resultat = 1
	for i in range(1, n + 1):
		resultat *= i
	return resultat

n = int(input("Entrez la valeur dont vous souhaitez obtenir la factorielle: "))
print(f"{n}! = {factorielle(n)}")

def coeff_binomial(n, k):
	fn = factorielle(n)
	fk = factorielle(k)
	n - k = i
	fi = factorielle(i)
	
	q = fn/((fi * fk)
	return fk
	

