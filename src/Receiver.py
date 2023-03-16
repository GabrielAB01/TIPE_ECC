import numpy as np
from random import randrange
from src.utils import createMatrixFromRow


class Receiver:
    def __init__(self, public):
        self.a = randrange(1, public["q"])

    def decodeMsg(self, public):
        # Reconstituer la matrice S (de dim 1,n)
        bP, X = public["bP"]
        S = X - self.a*bP  # (S + baP) - a(bP)

        # Retransformer S en une chaîne de caractères
        Q = createMatrixFromRow(S)

        # Q = AM => M = A^-1 * Q
        M = np.dot(
            np.int_(np.linalg.inv(public["A"])),
            Q
        )

        pointsArr = np.ndarray.flatten(M)  # Matrice (P1, P2, ... Pn)
        msg = public["pointsToString"](pointsArr)

        # Enlever les caractères nuls:
        return msg.rstrip('\x00')
