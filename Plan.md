# Plan partiel du TIPE sur les courbes elliptiques :

<style>
h2 {
	text-decoration: underline red 1px;
	font-style: italic;
	font-weight: 500
}
</style>

## 1. Logarithme discret et courbes elliptiques

- **Logarithme discret** sur $\mathbb{Z}/p\mathbb{Z}$ : Introduction puis extension à un groupe quelconque
- **Courbe elliptique** sur un corps $\mathbb{K}$.
- **Structure de groupe** de $E(\mathbb{K}) \cup \mathcal{O}$ :
  - Point de vue géométrique de la loi + (avec $\mathbb{K} = \mathbb{R}$)
  - Point de vue algébrique
- **Logarithme discret** sur $E(\mathbb{F}_p)$ : $n \in E(\mathbb{F}_p) \ tq\ nP = P + ... + P  = Q$
- **Programmation** : langage, méthode, choix…

## 2. ECC : Elliptic Curve Cryptography

- **Transmission** de message en cryptographie :
  - Principe général : clé publique et privée ([Diffie-Hellman](https://fr.wikipedia.org/wiki/%C3%89change_de_cl%C3%A9s_Diffie-Hellman))
  - Principe détaillé pour des courbes elliptiques ([Elliptic Curve Diffie Hellman](https://youtu.be/F3zzNa42-tQ?t=709))
- **Implémentation de la transmission** :
  - Algorithme 'Double and add' (Addition et doublement) pour calculer $nP$ en $O(log(n))$
  - Traduction du message en un point de $E(\mathbb{F}_p) \rightarrow$ Méthode matricielle
  - Décryptage du message par le récepteur
- **Interception du message** :
  - « Brute Force »
  - Algorithme de décryptage plus efficace : ...

## 3. Application à un cas concret :

- Valeur des paramètres : $p, a, b$
- Choix du message (longueur)
- Conversion de la chaîne de caractères en nombre
- Traduction de cet entier sur la courbe
- Comparaison des différents algos d’interception du message

## 4. Autres :

- Signature du message pour assurer l’intégrité de la transmission
- ECDSA : Elliptic curve digital signature algorithm, algorithme de signature électronique à clé publique utilisé par certaines cryptomonnaies (Bitcoin, Ethereum) ([ECDSA](https://fr.wikipedia.org/wiki/Elliptic_curve_digital_signature_algorithm))
