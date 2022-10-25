from src.CurvePoint import CurvePoint


class Encoder:
	
	@staticmethod
	def encode(s: str) -> int:
		sBytes = s.encode("utf-8")
		sInt = int.from_bytes(sBytes, byteorder="big")
		return sInt


	@staticmethod
	def decode(n: int) -> str:
		sBytes = n.to_bytes(((n.bit_length() + 7) // 8), byteorder="big")
		s = sBytes.decode("utf-8")
		return s

	
	def __init__(self, msg, P):
		self.msg = msg
		self.nMsg = Encoder.encode(msg)
		self.P = P
		self.getPointsArray()
	
	
	def getPointsArray(self):
		alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
		dico = {} # lettre -> Point sur la courbe
		point = CurvePoint(self.P.a, self.P.b) # neutre
		
		for l in alphabet:
			dico[l] = point
			point = point + self.P
		
		self.dico = dico

		# Inverser le dictionaire : 
		self.dico_inv = {f"{P.x},{P.y}": l for l, P in dico.items()}

		
	
	def stringToArray(self):
		return [self.dico[l] for l in self.msg]
	