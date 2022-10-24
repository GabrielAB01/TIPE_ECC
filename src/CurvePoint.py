from src.constants import p
from src.IntModP import IntModP

class CurvePoint:
    def __init__(self, a, b, x=None, y=None):
        self.a = IntModP(a)
        self.b = IntModP(b)

        if x==None and y==None :
            self.x = x
            self.y = y
        else:
            self.x = IntModP(x) 
            self.y = IntModP(y)

    # Affichage lors d'un print
    def __str__(self):
        if self.isNeutral():
            return f"Neutre de E(Z/{p}Z)"
        return f"Point de E(Z/{p}Z) : ({self.x}, {self.y})"

    # Egalité de 2 points
    def __eq__(self, q):
        return self.x == q.x and self.y == q.y

    def isNeutral(self):
        return self.x == None and self.y == None

    def __add__(self, q):
        # Si un des 2 est le neutre
        if self.isNeutral():
            return q
        if q.isNeutral():
            return self

        # Si Q=-P
        if q.x == self.x and q.y == -self.y:
            return CurvePoint(self.a, self.b)  # Element neutre

        # Calcul de L (pente)
        L = IntModP(0)
        x1, y1 = self.x, self.y
        x2, y2 = q.x, q.y
        if self == q:
            L = (x1**2 * 3 + self.a) / (y1 * 2)  # Tangente à la courbe en P
        else:
            L = (y1 - y2) / (x1 - x2)  # Coeff directeur de la droite (PQ)

        # Coordonnées du nouveau point :
        x3 = (L**2 - x1 - x2)
        y3 = (-L * x3 - (y1 - L*x1)) 
        return CurvePoint(self.a, self.b,x3, y3)  # Element neutre

    # Produit P*n avec l'algorithme 'Double and add'
    def __mul__(self, n):
        if type(n) != int or n<=0 :
            raise Exception("n doit être un entier positif !")

        bits = bin(n) # Représentation en binaire de n
        result = CurvePoint(self.a, self.b) # Neutre
        current = self # Vaut toujours 2^i * P

        for i in range(len(bits)-1, 1, -1): # On commence par le bit de poids faible
            bit = int(bits[i])
            if bit == 1 :
                result += current
            current = current + current
        return result     

    # Produit n*P :  
    def __rmul__(self, n):
        return self * n
  