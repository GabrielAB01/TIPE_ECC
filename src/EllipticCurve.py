import matplotlib.pyplot as plt
from math import sqrt

from src.IntModP import IntModP
from src.CurvePoint import CurvePoint


class EllipticCurve:
    """ Courbe elliptique sur Z/pZ """

    def __init__(self, a, b):  # Initialisation des paramètres de la courbe
        self.a = IntModP(a)
        self.b = IntModP(b)
        self.points = []

        if self.discriminant() == 0:
            raise Exception("Le discriminant est nul !")

    def discriminant(self):
        return (self.a**3 * 4 + self.b**2 * 27) * -16

    # Affichage lors d'un print(E)
    def __str__(self) -> str:
        return f"y^2 = x^3 + {str(self.a).split(' ')[0]}x + {self.b}"

    # Renvoie un nouveau point de la courbe
    def newPoint(self, x=None, y=None):
        return CurvePoint(self.a, self.b, x, y)

    # Création de la liste self.points
    def createPoints(self, q=None):
        p = q or IntModP.p
        a = int(self.a)  # On retransforme en int pour accélérer les calculs car le %p se fait dans le =
        b = int(self.b)
        points = [self.newPoint()]  # Elément neutre

        for x in range(p):
            for y in range(p):
                if (y*y - (x*x*x + a*x + b)) % p == 0:  # x*x*x est plus rapide que x**3 !!
                    points.append(self.newPoint(x, y))

        self.points = points

    # Affiche les points de la courbe
    def drawPoints(self):
        x_list = [el.x for el in self.points]
        y_list = [el.y for el in self.points]
        plt.figure(1, figsize=(10, 10))
        plt.axis([-0.5, IntModP.p-0.5, -0.5, IntModP.p - 0.5])
        plt.grid()
        plt.text(0, 0.5, f"${self.__str__()}$", size="large", color="blue", family='cursive',)
        plt.plot(x_list, y_list, 'ro', markersize=12)
        plt.show()

    # Print tous les points de la courbe
    def printPoints(self):
        points = map(lambda el: (el.x, el.y), self.points)
        print(list(points))

    # Renvoie un point d'ordre order après avoir créé les points :
    def getGeneratorPoint(self, order):
        # L'ordre du groupe est un multiple de l'ordre d'un élément
        if len(self.points) % order != 0 or order > len(self.points):
            raise Exception("L'ordre d'un élément doit diviser l'ordre du groupe !")

        for P in self.points:
            # On calcule l'ordre en se limitant à o = order
            o = 1
            Q = P
            while (not Q.isNeutral()) and o <= order+1:
                Q = Q + P
                o += 1

            if o == order:
                return P

        raise Exception(f"Pas de points d'ordre {order} sur la courbe {self}")

    # Renvoie un point d'ordre au moins order (sans avoir créé self.points)
    def getPointOfOrder(self, order):
        p = IntModP.p
        if order >= p + 1 + 2 * sqrt(p):
            raise Exception("Ordre trop grand (Th de Hasse)")

        a = int(self.a)  # On retransforme en int pour accélérer les calculs car le %p se fait dans le =
        b = int(self.b)

        for x in range(p):
            for y in range(p):
                if (y*y - (x*x*x + a*x + b)) % p == 0:
                    P = CurvePoint(a, b, x, y)
                    if P.order() >= order:
                        return P

    # Retourne les n premiers nombres premiers
    def getPrimesNumber(self, n: int):
        primes = [2]
        i = 1
        p = 3
        while i < n:
            if all([p % d for d in primes]):
                primes.append(p)
                i += 1
            p += 2
        return primes

    # Affiche le graphe ep <= sqrt(p)
    def test_hasse(self):
        primes = self.getPrimesNumber(500)
        ep_list = []
        y_list = []
        y2_list = []
        for p in primes:
            self.createPoints(p)
            ep_list.append(p+1 - len(self.points))
            y_list.append(2*sqrt(p))
            y2_list.append(-2*sqrt(p))

        plt.figure(1, figsize=(10, 10))
        plt.grid()
        plt.plot(ep_list, 'ro', markersize=2)
        plt.plot(y_list, markersize=2)
        plt.plot(y2_list, markersize=2)
        plt.show()
