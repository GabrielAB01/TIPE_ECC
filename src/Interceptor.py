from math import ceil, sqrt
from src.CurvePoint import CurvePoint
from src.Receiver import Receiver

class Interceptor:
	def __init__(self):
		pass

	def decodeMsg(self, public):
		# But Trouver a avec aP et P (log discret)
		# Puis calculer S = (S + baP) - a(bP) (comme le Receiver)

		a = self.logDiscret(public['P'], public["aP"])
		R = Receiver(public, False)

	
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
				print(i, j)
				return (i + m*j)
			temp_R -= R
		
		raise Exception(f"Le log discret de {Q} en base {base} n'a pas été trouvé ")

