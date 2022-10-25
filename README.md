# TIPE - Cryptographie et courbes elliptiques

<style>
h2{
	text-decoration: underline red 1px;
}
</style>

## Contenu du notebook Jupyter

- ### Classe `IntModP(int)` :

  > Opérations sur les entiers de $\mathbb{Z}/p\mathbb{Z}$

  - Pour calculer l'inverse : Théorème de Fermat : $n^{p-1} = 1 \ [p] \implies n * (n^{p-2}) = 1\  [p] \implies n^{-1} = n^{p-2}$
  - Création de la fonction `pow(n)` qui implémente l'exponentiation rapide

<br>

- ### Classe `CurvePoint` :

  > Point sur une courbe elliptique de $\mathbb{Z}/p\mathbb{Z}$

  - Addition de 2 points
  - Produit par un entier : Calcul de $nP$ par l'algorithme _Double and Add_

<br>

- ### Classe `EllipticCurve` :

  > Représente une courbe elliptique de paramètres $\ a, b \in \mathbb{Z}/p\mathbb{Z}$ ie d'équation $\ y^2 = x^3 + ax + b \ [p]$

  - Calcul du discriminant
  - Création de la liste des points de la courbe
  - Affichage des points dans le plan

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

<br>

---

<br>

> ## Gabriel Abenhaim
>
> > La Martinière Monplaisir - MP\*
>
> > Année 2022/2023
