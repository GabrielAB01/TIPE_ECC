import numpy as np
from random import randrange
from src.utils import createMatrixFromRow


class Receiver:
    def __init__(self, public):
        self.b = randrange(1, public["q"])

        # Publier bP :
        public["bP"] = self.b * public["P"]

    def decodeMsg(self, public: dict) -> str:
        # Reconstituer la matrice S (de dim 1,n)
        bP, X = public["aP"]
        S = X - self.b*bP  # (S + baP) - b(aP)

        # Retransformer S en une chaîne de caractères
        Q = createMatrixFromRow(S)

        # Q = AM => M = A^-1 * Q
        M = np.dot(
            np.int_(np.linalg.inv(public["A"])),
            Q
        )

        pointsArr = np.ndarray.flatten(M)  # Matrice (P1, P2, ... Pn)
        msg = public["pointsToString"](pointsArr)

        # Enlever les espaces ajoutés à la fin
        return msg.rstrip()
