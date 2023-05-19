import numpy as np
from random import randrange
from src.utils import createMatrixFromRow


class Emitter:
    def __init__(self, msg, public: dict):
        self.msg = msg
        self.a = randrange(1, public["q"])

    def encodeMsg(self, public: dict) -> None:
        Pi = self.createPointsArray(public)  # Listes des Pi
        M = createMatrixFromRow(Pi)
        Q = np.dot(public["A"], M)

        # S est la donnée à transmettre (de dimension 1,n)
        S = np.ndarray.flatten(Q)

        # Publier le couple (aP, S + a(bP)) - Le 2ème élement est une liste
        public["aP"] = (self.a*public["P"], S + self.a*public["bP"])

    # Créer la liste des Pi en complétant avec des "neutres"
    def createPointsArray(self, public):
        arr = public["stringToPoints"](self.msg)
        n = len(arr)

        # Compléter avec des caractères nuls pour que len(arr) == 3
        if n % 3 != 0:
            neutralPoint = public["P"].getNeutral()
            arr = arr + ([neutralPoint] * (3 - n % 3))

        return arr
