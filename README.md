# TIPE - Cryptographie et courbes elliptiques

## Contenu du notebook Jupyter

- ### Classe `IntModP(int)` :

  > Opérations sur les entiers de $\mathbb{Z}/p\mathbb{Z}$
  - Addition, Soustraction, Multiplication
  - Pour calculer l'inverse : Théorème de Fermat : $n^{p-1} = 1 \ [p] \implies n^{-1} = n^{p-2}$
  - Création de la fonction `pow(n)` qui implémente l'exponentiation rapide

<br>

- ### Classe `CurvePoint` :

  > Point sur une courbe elliptique de $\mathbb{Z}/p\mathbb{Z}$

  - Addition de 2 points
  - Produit par un entier : Calcul de $nP$ par l'algorithme _Double and Add_
  - Calcul de l'ordre d'un point
  
<br>

- ### Classe `EllipticCurve` :

  > Représente une courbe elliptique de paramètres $\ a, b \in \mathbb{Z}/p\mathbb{Z}$ ie d'équation $\ y^2 = x^3 + ax + b \ [p]$

  - Calcul du discriminant
  - Création de la liste des points de la courbe
  - Affichage des points dans le plan
  - Fonction `getGeneratorPoint(order)` pour récupérer un point de la courbe d'ordre `order`.
  - Fonction `getPointOfOrder(order)` pour récupérer un point de la courbe d'ordre au moins `order`. (Plus rapide que la précédente)
  
<br>

- ### Classe `Emitter` :
  > Permet de chiffrer un message

  - `__init__(msg, public)` : Initialise la clé privée de l'émetteur en fonction de l'ordre du point générateur.
  - `encodeMsg(public)` : Ajoute une entrée dans le dictionnaire `public` contenant la clé publique de chiffrement.
  
<br>

- ### Classe `Receiver` :
  > Permet de déchiffrer un message

  - `__init__(msg, public)` : Initialise la clé privée du récepteur en fonction de l'ordre du point générateur.
  - `encodeMsg(public)` : Retourne le message déchiffré à l'aide la clé du dictionnaire `public`.

  
<br>

## Déroulé Opérationnel du TIPE (DOT)

### Septembre :

- Début de la programmation : classes principales et opérations ([elliptic_curves.pdf](https://github.com/GabrielAB01/TIPE_ECC/blob/master/docs/elliptic_curves.pdf))
- Problèmes : Comment lier un message à un point de la courbe ?
  - Méthode avec les probas ? $\rightarrow$ Bcp de points à admettre
  - Méthode avec les matrices ? $\rightarrow$ Semble efficace et pas trop dur à mettre en place ([Traduction_message_matrices.pdf](https://github.com/GabrielAB01/TIPE_ECC/blob/master/docs/Traduction_message_matrices.pdf))

### Octobre :

- Implémentation de l'algorithme complet de transmission d'un message
  - Point sur la courbe : On code la phrase en une matrice ligne de points
  - On calcule les produits matriciels et on transmet une matrice ligne S
  - On effectue les opérations inverses pour décoder

### Novembre :

- Quelques algos de log discret
  - Brute force
  - Baby-step Giant-step
  - Algorithme $\rho$ de Pollard
  - ~~Algorithme de Pohlig-Hellman~~

### Décembre - Janvier :
- Rédaction du MCOT : Lien avec le thème, Mots-clés, Plan, Problématique, Bibliographie commentée


### Février :
- Début de la préparation de la présentation :
  - Thème Beamer
  - Plan détaillé
  - Partie "théorique" : définition de courbe elliptique + Problème du log discret

### Mars : 
- Algorithmes d'exponentiation rapide et _Double and Add_ écrit en pseudo-code
- Algorithmes de résolution du log discret :
  - _Brute Force_
- Exemples de courbes en Latex (discriminant nul)
- Exemple somme de 2 points dans $\mathbb{R}$
- Diagrammes pour expliquer Diffie-Hellman et El Gamal

<br>

---
## **Avril -> 12 Mai : _Écrits_**
---

<br>

### Mai - TODO :
- Algorithmes de log discret en pseudo-code + screens
- Signatures et/ou attaques possibles (MITM par exemple) (+ solutions ?)
- Exemple de transmission concrète (screens)
- Influence des paramètres sur le tps

---

<br>

> ## Gabriel Abenhaim
>
> > La Martinière Monplaisir - MP\*
>
> > Année 2022/2023
