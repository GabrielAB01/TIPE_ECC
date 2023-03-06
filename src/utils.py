import numpy as np
from src.CurvePoint import CurvePoint


def createMatrixFromRow(row):
    n = len(row)
    if (n % 3) != 0:
        raise Exception('La ligne doit avoir une taille multiple de 3')

    r = int(n/3)
    return np.array([
        [row[j] for j in range(r)],
        [row[j] for j in range(r, 2*r)],
        [row[j] for j in range(2*r, n)],
    ])


def displayPointsArray(arr):
    print([(el.x, el.y) for el in arr])


# Placer les points avec l'alphabet
def createMaps(P: CurvePoint):
    alphabet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789,;:!?./%§²&é'(-è_çà)=~#{[|`^@]}\\\"°+=êïîöôù*µ$£€ÉÊË"

    letterToPoint = {}  # Lettre -> Point sur la courbe
    pointToLetter = {}  # Point sur la courbe --> Lettre
    point = P.getNeutral()

    for l in alphabet:
        letterToPoint[l] = point
        pointToLetter[point.getCoords()] = l
        point = point + P

    def stringToPoints(str):
        return [letterToPoint[l] for l in str]

    def pointsToString(arr):
        msg = [pointToLetter[Q.getCoords()] for Q in arr]
        return "".join(msg)

    return (stringToPoints, pointsToString)

# Placer les points avec les codes ASCII


def createMaps_old(P: CurvePoint):
    letterToPoint = {}  # Lettre -> Point sur la courbe
    pointToLetter = {}  # Point sur la courbe --> Lettre
    point = P.getNeutral()

    # Pour tous les codes ASCII
    for i in range(128):
        l = chr(i)
        letterToPoint[l] = point
        pointToLetter[point.getCoords()] = l
        point = point + P
    print(letterToPoint)

    def stringToPoints(str):
        return [letterToPoint[l] for l in str]

    def pointsToString(arr):
        msg = [pointToLetter[Q.getCoords()] for Q in arr]
        return "".join(msg)

    return (stringToPoints, pointsToString)


def createMatrixA():
    A = np.array([
        [-1, 5, -1],
        [-2, 11, 7],
        [1, -5, 2]
    ], dtype=int)
    # A doit être de déterminant 1 ou -1
    if abs(np.linalg.det(A)) != 1:
        raise Exception('A doit être de déterminant 1 ou -1')
    return A


def initPublic(P: CurvePoint):
    stringToPoints, pointsToString = createMaps(P)
    return {
        "stringToPoints": stringToPoints,
        "pointsToString": pointsToString,
        "P": P,
        "q": P.order(),
        "A": createMatrixA()
    }


def primeFactors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            n = n//i
            factors.append(i)
        else:
            i += 1

    if n > 1:
        factors.append(n)

    return factors
