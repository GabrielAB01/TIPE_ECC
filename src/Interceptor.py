import numpy as np
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

	
	def log_discret(self, base, Q: CurvePoint):
		if Q.isNeutral():
			return 0

		i = 1
		temp = base

		while temp != Q and i<=100_000:
			i += 1
			temp = temp + base

		if temp!=Q:
			raise Exception(f"Le log discret de {Q} en base {base} n'a pas été trouvé ")
		
		return i
