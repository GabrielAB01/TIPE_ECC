import numpy as np
from random import randrange
from src.utils import createMatrixFromRow


class Emitter:
    def __init__(self, msg, public: dict):
        self.msg = msg
        self.b = randrange(1, public["q"])

    def encodeMsg(self, public):
        pointsArr = self.createPointsArray(public)
        M = createMatrixFromRow(pointsArr)

        Q = np.dot(public["A"], M)

        # S est la donnée à transmettre ! (de dimension 1,n)
        S = np.ndarray.flatten(Q)

        # Publier le couple (bP, S + b(aP)) - Le 2ème élement est une matrice
        public["bP"] = (self.b*public["P"], S + self.b*public["aP"])

    def createPointsArray(self, public):
        arr = public["stringToPoints"](self.msg)
        n = len(arr)

        # Compléter avec des caractères nuls pour que len(arr) == 3
        if n % 3 != 0:
            neutralPoint = public["P"].getNeutral()
            arr = arr + ([neutralPoint] * (3 - n % 3))

        return arr
