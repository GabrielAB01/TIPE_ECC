from src.IntModP import IntModP

class CurvePoint:
    def __init__(self, a, b, x=None, y=None):
        self.a = IntModP(a)
        self.b = IntModP(b)
        self.o = False

        if x is None or y is None :
            self.x = x
            self.y = y
        else:
            self.x = IntModP(x) 
            self.y = IntModP(y)

    # Affichage lors d'un print
    def __str__(self):
        p = IntModP.p
        if self.isNeutral():
            return f"Neutre de E(Z/{p}Z)"
        return f"Point de E(Z/{p}Z) : ({self.x}, {self.y})"

    # Egalité de 2 points
    def __eq__(self, q):
        return self.x == q.x and self.y == q.y

    def isNeutral(self):
        return self.x is None and self.y is None

    def getNeutral(self):
        return CurvePoint(self.a, self.b)

    def __add__(self, q): # O(log(p)) car on calcule l'inverse d'un entier mod p
        # Si un des 2 est le neutre
        if self.isNeutral():
            return q
        if q.isNeutral():
            return self

        # Si Q=-P
        if q.x == self.x and q.y == -self.y:
            return self.getNeutral()

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
        return CurvePoint(self.a, self.b, x3, y3)

    # Produit P*n avec l'algorithme 'Double and add'
    def __mul__(self, n): # O(log(n)log(p)) car la somme de points est en log(p)
        if type(n) != int :
            raise Exception("n doit être un entier positif !")

        if n==0 :
            return self.getNeutral()
        elif n<0 :
            return -(self * (-n))

        bits = bin(n) # Représentation en binaire de n
        result = self.getNeutral() # Neutre
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

    # Opposé -P
    def __neg__(self):
        if self.isNeutral():
            return self
        return CurvePoint(self.a, self.b, self.x, -self.y)
    
    def __sub__(self, q):
        return self + (-q)

    def order(self):
        if self.o:
            return self.o

        o = 1  #! 0 est d'ordre 1 et si 2*P=0 alors P est d'ordre 2
        P = self
        while (not P.isNeutral()) and o < 1_000_000:
            P = P + self
            o+=1

        self.o = o
        return o

    def getCoords(self):
        x = str(self.x).split(" ")[0]
        y = str(self.y).split(" ")[0]
        return f"{x},{y}"
  