from math import ceil, sqrt
from random import randrange

from src.CurvePoint import CurvePoint
from src.IntModP import IntModP

class LogDiscret:
	def __init__(self):
		pass

	def decodeMsg(self, public):
		# But Trouver a avec aP et P (log discret)
		a = self.logDiscret(public['P'], public["aP"])

	
	def log_discret(self, base: CurvePoint, Q: CurvePoint): # O(p*log(p))
		if Q.isNeutral():
			return base.order()

		i = 1
		temp = base

		while temp != Q and i<=100_000:
			i += 1
			temp = temp + base

		if temp!=Q:
			raise Exception(f"Le log discret de {Q} en base {base} n'a pas été trouvé ")
		
		return i

	def baby_step_giant_step(self, base: CurvePoint, Q:CurvePoint) -> int: # O(log(p) * sqrt(n)) avec l'ordre de la base
		q = base.order()
		m = ceil(sqrt(q))
		R = m * base

		baby_step = {}

		temp_P = base.getNeutral()
		for i in range(m):
			baby_step[temp_P] = i
			temp_P += base
		
		
		temp_R = Q
		for j in range(m):
			# Si Q-jR = iP <=> Q = iP + jR <=> Q = (i+mj)P
			if temp_R in baby_step:
				i = baby_step[temp_R]
				return (i + m*j)
			temp_R -= R
		
		raise Exception(f"Le log discret de {Q} en base {base} n'a pas été trouvé ")
	

	def rho_pollard(self, base: CurvePoint, Q: CurvePoint):
		# Avec Pohlig-Hellman on peut se ramener à P.o premier
		# Donc on considère ici que q = P.o est premier
		p = IntModP.p
		def f(_):
			return (randrange(0, p), randrange(0,p))
		
		def R(U):
			a,b = U
			return a*base + b*Q

		Ui = (randrange(1, p), randrange(1, p))
		Ri = R(Ui)
		rho = {}
		
		i = 0
		while not (Ri in rho) and i<=20000:
			rho[Ri] = Ui
			Ui = f(Ui)
			Ri = R(Ui)
			i+=1
		
		# On a ajP + bjQ = aiP + biQ <=> (aj - ai)P = (bi-bj)Q <=> logP(Q) = (aj-ai)(bi-bj)^-1
		aj, bj = rho[Ri]
		ai, bi = Ui
		IntModP.p = base.order()
		result = IntModP(aj-ai) * IntModP(bi-bj).inverse()
		IntModP.p = p
		return result
	
	def rho_pollard_floyd(self, base: CurvePoint, Q: CurvePoint):
		p = IntModP.p
		def f(U):
			aj,bj = U
			a,b = base.a, base.b # Paramètres de la courbe
			return ((a*aj+b)%p, (a*bj+b)%p)
		
		def R(U):
			a,b = U
			return a*base + b*Q

		Uj = (randrange(1, p), randrange(1, p))
		U2j = f(Uj)
		
		i = 0
		while R(Uj)!=R(U2j) and i<=20000:
			Uj = f(Uj)
			U2j = f(f(U2j))
			i+=1
		print("i = ", i)
		
		# On a ajP + bjQ = a2jP + b2jQ <=> (aj - a2j)P = (b2j-bj)Q <=> logP(Q) = (aj-a2j)(b2j-bj)^-1
		aj, bj = Uj
		a2j, b2j = U2j
		IntModP.p = base.order()
		result = IntModP(aj-a2j) * (1/IntModP(b2j-bj))
		IntModP.p = p
		return result






