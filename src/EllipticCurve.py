import matplotlib.pyplot as plt
from math import sqrt

from src.IntModP import IntModP
from src.CurvePoint import CurvePoint


class EllipticCurve:
    def __init__(self, a, b):
        self.a = IntModP(a)
        self.b = IntModP(b)
        self.points = []

        if self.discriminant() == 0:
            raise Exception("Le discriminant est nul !")

        # self.createPoints()

    def discriminant(self):
        return (self.a**3 * 4 + self.b**2 * 27) * -16

    def __str__(self) -> str:
        return f"y^2 = x^3 + {self.a}x + {self.b}"

    def newPoint(self, x=None, y=None):
        return CurvePoint(self.a, self.b, x, y)

    def createPoints(self):
        p = IntModP.p
        a = int(self.a)  # On retransforme en int pour accélérer les calculs car le %p se fait dans le =
        b = int(self.b)
        points = [self.newPoint()]  # Elément neutre

        for x in range(p):
            for y in range(p):
                if (y*y - (x*x*x + a*x + b)) % p == 0:  # x*x*x est plus rapide que x**3 !!
                    points.append(self.newPoint(x, y))

        self.points = points

    def drawPoints(self):
        x_list = [el.x for el in self.points]
        y_list = [el.y for el in self.points]
        # print(x_list, y_list)
        plt.figure(1, figsize=(10, 10))
        plt.axis([-0.5, IntModP.p-0.5, -0.5, IntModP.p - 0.5])
        plt.grid()
        plt.text(0, 0.5, f"${self.__str__()}$", size="large", color="blue", family='cursive',)
        plt.plot(x_list, y_list, 'ro', markersize=12)
        # plt.savefig("graph.jpg")
        plt.show()

    def printPoints(self):
        points = map(lambda el: (el.x, el.y), self.points)
        print(list(points))

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
                    if P.order() > order:
                        return P
