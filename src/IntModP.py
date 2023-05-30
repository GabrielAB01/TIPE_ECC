# Exponentiation rapide
def expo_rapide(x: float, n: int):
    if n == 0:
        return 1
    if n % 2 == 0:
        return expo_rapide(x, n/2)**2
    else:
        return x * expo_rapide(x, (n-1)/2)**2


class IntModP(int):
    """ Représente un entier et ses opérations modulo p """
    p = 0

    def __new__(cls, n):
        return int.__new__(cls, n % IntModP.p)

    # Affichage en console
    def __str__(self):
        return int.__str__(self) + f" [{IntModP.p}]"

    # Opposé mod p
    def __neg__(self):
        return IntModP(int.__neg__(self))

    # Addition modulo p
    def __add__(self, q):
        return IntModP(int.__add__(self, q))

    # Soustraction mod p
    def __sub__(self, q):
        return IntModP(int.__sub__(self, q))

    # Multiplication mod p
    def __mul__(self, q):
        return IntModP(int.__mul__(self, q))

    # Puissance mod p
    def __pow__(self, q):
        if q >= 0:
            return IntModP(int.__pow__(self, q))
        else:
            return IntModP(int.__pow__(self.inverse(), -q))

    # Division mod p
    def __truediv__(self, q):
        return IntModP(self * q.inverse())

    def inverse(self):  # O(log(p))
        return IntModP(expo_rapide(self, IntModP.p-2))  # Théorème de Fermat : n**(p-2) * n = 1 [p]

    def inverse_old(self):
        p = IntModP.p
        for i in range(p):
            if (self * i) % p == 1:
                return IntModP(i)
        raise ZeroDivisionError(f"{self} n'est pas inversible")
