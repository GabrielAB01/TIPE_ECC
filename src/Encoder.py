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

	