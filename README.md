# TIPE - Cryptographie et courbes elliptiques

## Contenu du notebook Jupyter :

- ### Classe `IntModP(int)` :

  _Opérations sur les entiers de_ $\mathbb{Z}/p\mathbb{Z}$

  - Pour calculer l'inverse : Théorème de Fermat : $n^{p-1} = 1 \ [p] \implies n * (n^{p-2}) = 1\  [p] \implies n^{-1} = n^{p-2}$
  - Utilisation de la fonction `pow(n)` pour utiliser l'exponentiation rapide

<br>

- ### Classe `CurvePoint` :

  _Point sur une courbe elliptique de_ $\mathbb{Z}/p\mathbb{Z}$

  - Addition de 2 points
  - Produit par un entier : Calcul de $nP$ par l'algorithme _Double and Add_

<br>

- ### Classe `EllipticCurve` :

  _Représente une courbe elliptique de paramètres_ $\ a, b \in \mathbb{Z}/p\mathbb{Z} \ $ _ie d'équation_ $\ y^2 = x^3 + ax + b \ [p]$

  - Calcul du discriminant
  - Création de la liste des points de la courbe
  - Affichage des points dans le plan

## Déroulé

### Septembre :

- Début de la programmation : classes principales et opérations ([elliptic_curves.pdf](https://github.com/GabrielAB01/TIPE_ECC/blob/master/elliptic_curves.pdf))
- Problèmes : Comment lier un message à un point de la courbe ?
  - Méthode avec les probas ? $\rightarrow$ Bcp de points à admettre
  - Méthode avec les matrices ? $\rightarrow$ Semble efficace et pas trop dur à mettre en place

### Octobre :

- Implémentation de l'algorithme'
<br />
<br />
<br />
<hr/>

### _<u>Gabriel Abenhaim</u> - MP\* - 2022/2023_
