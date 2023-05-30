from math import ceil, sqrt
from random import randrange

from src.CurvePoint import CurvePoint
from src.IntModP import IntModP


class LogDiscret:
    def __init__(self):
        pass

    # Algorithme Brute Force
    def log_discret(self, base: CurvePoint, Q: CurvePoint) -> int:  # O(p*log(p))
        # Si Q=O alors on retourne l'ordre de la base
        if Q.isNeutral():
            return base.order()

        i = 1
        temp = base
        # On calcule P+P+... jusqu'à tomber sur Q
        while temp != Q and i <= 1_000_000:
            i += 1
            temp = temp + base

        if temp != Q:
            raise Exception(f"Le log discret de {Q} en base {base} n'a pas été trouvé ")

        return i

    # Log discret par l'algorithme Baby-step Giant-step
    # O(log(p) * sqrt(q)) avec q l'ordre de la base
    def baby_step_giant_step(self, base: CurvePoint, Q: CurvePoint) -> int:
        q = base.order()
        m = ceil(sqrt(q))
        baby_step = {}  # Dictionnaire des (i, iP)

        # Baby Step
        temp_P = base.getNeutral()  # Variable temporaire
        for i in range(m):  # Remplissage du dictionnaire
            baby_step[temp_P] = i
            temp_P += base

        # Giant Step
        R = m * base
        temp_R = Q
        for j in range(m):
            # Si Q-jR = iP <=> Q = iP + jR <=> Q = (i+mj)P
            if temp_R in baby_step:
                i = baby_step[temp_R]
                return (i + m*j)
            temp_R -= R

        raise Exception(f"Le log discret de {Q} en base {base} n'a pas été trouvé ")

    # Renvoie l'ordre de P : n tel que O=nP
    def order_baby_step(self, P: CurvePoint) -> int:
        p = IntModP.p
        q = p+1+2*sqrt(p)  # P.o < |E| < p+1+2sqrt(p) (Hasse)
        m = ceil(sqrt(q))
        R = m * P
        baby_step = {}

        temp_P = P
        for i in range(1, m):
            baby_step[temp_P] = i
            temp_P += P

        temp_R = P.getNeutral()
        for j in range(m):
            # Si Q-jR = iP <=> Q = iP + jR <=> Q = (i+mj)P
            if temp_R in baby_step:
                i = baby_step[temp_R]
                return (i + m*j)
            temp_R -= R
        return "Erreur"

    # Log discret par l'algorithme rho de Pollard
    def rho_pollard(self, base: CurvePoint, Q: CurvePoint):
        # On considère ici que q = P.o est premier
        p = IntModP.p

        def f(a, b):  # Fonction pseudo-aléatoire
            return ((a**2+1) % p, (b**2+1) % p)

        def R(a, b):  # Renvoie aP+bQ
            return a*base + b*Q

        ai, bi = (randrange(1, p), randrange(1, p))  # Valeurs initiales a0 et b0
        Ri = R(ai, bi)  # Ri = aiP + biQ
        rho = {}  # Dictionnaire des Ri pour sauvegarder les valeurs

        i = 0
        while not (Ri in rho) and i <= 1_000_000:
            rho[Ri] = (ai, bi)
            ai, bi = f(ai, bi)
            Ri = R(ai, bi)
            i += 1

        # On a ajP + bjQ = aiP + biQ <=> (aj - ai)P = (bi-bj)Q <=> logP(Q) = (aj-ai)(bi-bj)^-1
        aj, bj = rho[Ri]  # Point de la collision
        print(aj, bj, R(aj, bj))
        print(ai, bi, R(ai, bi))
        IntModP.p = base.order()
        result = IntModP(aj-ai) * IntModP(bi-bj).inverse()
        IntModP.p = p
        return result

    # UNUSED
    def rho_pollard_floyd(self, base: CurvePoint, Q: CurvePoint):
        p = IntModP.p

        def f(U):
            aj, bj = U
            a, b = base.a, base.b  # Paramètres de la courbe
            return ((a*aj+b) % p, (a*bj+b) % p)

        def R(U):
            a, b = U
            return a*base + b*Q

        Uj = (randrange(1, p), randrange(1, p))
        U2j = f(Uj)

        i = 0
        while R(Uj) != R(U2j) and i <= 20000:
            Uj = f(Uj)
            U2j = f(f(U2j))
            i += 1
        print("i = ", i)

        # On a ajP + bjQ = a2jP + b2jQ <=> (aj - a2j)P = (b2j-bj)Q <=> logP(Q) = (aj-a2j)(b2j-bj)^-1
        aj, bj = Uj
        a2j, b2j = U2j
        IntModP.p = base.order()
        result = IntModP(aj-a2j) * (1/IntModP(b2j-bj))
        IntModP.p = p
        return result
