import numpy as np
from random import randrange
from src.utils import createMatrixFromRow


class Receiver:
    """Permet de recevoir un message"""

    def __init__(self, public):
        self.b = randrange(1, public["q"])  # Clé privée
        public["bP"] = self.b * public["P"]  # Publier bP

    # Déchiffre le message à partir des données du dictionnaire public.
    def decodeMsg(self, public: dict) -> str:
        # Reconstituer la matrice S (de dim 1,n)
        bP, X = public["aP"]
        S = X - self.b*bP  # (S + baP) - b(aP)

        # Recréer la liste des Pi :
        Q = createMatrixFromRow(S)
        # M = A^-1 * Q
        M = np.dot(
            np.int_(np.linalg.inv(public["A"])),
            Q)
        Pi = np.ndarray.flatten(M)  # Liste (P1, P2, ... Pn)
        msg = public["pointsToString"](Pi)

        return msg.rstrip()  # rstrip() sert à enlever les espaces à la fin
