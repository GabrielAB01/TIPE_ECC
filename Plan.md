# Plan partiel du TIPE sur les courbes elliptiques :

<!-- TOC -->

- [Plan](#plan-partiel-du-tipe-sur-les-courbes-elliptiques-)
  - [1. Logarithme discret et courbes elliptiques](#1-logarithme-discret-et-courbes-elliptiques)
  - [2. ECC : Elliptic Curve Cryptography](#2-ecc--elliptic-curve-cryptography)
  - [3. Application à un cas concret :](#3-application--un-cas-concret-)
  - [4. Autres :](#4-autres-)
  <!-- TOC -->

<style>
h2 {
	text-decoration: underline red 1px;
	font-style: italic;
	font-weight: 500
}
</style>

## 1. Logarithme discret et courbes elliptiques

- **Logarithme discret** sur un groupe quelconque
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
  - Application de Diffie-Hellman : [Cryptosystème de ElGamal](https://fr.wikipedia.org/wiki/Cryptosyst%C3%A8me_de_ElGamal)
- **Implémentation de la transmission** :
  - Algorithme 'Double and add' (Addition et doublement) pour calculer $nP$ en $O(log(n)log(p))$
  - Traduction du message en un point de $E(\mathbb{F}_p) \rightarrow$ Méthode matricielle
  - Décryptage du message par le récepteur
- **Interception du message - Log discret** :
  - « Brute Force »
  - Baby-step Giant-step
  - ~~Algorithme de Pohlig-Hellman~~
  - Algorithme $\rho$ de Pollard

## 3. Application à un cas concret :

- Influence de la valeur des paramètres : $p, a, b$
- Comparaison des différents algos de log discret

## 4. Autres :

- Signature du message pour assurer l’intégrité de la transmission
- ECDSA : Algorithme de signature électronique à clé publique utilisé par certaines cryptomonnaies ([ECDSA](https://fr.wikipedia.org/wiki/Elliptic_curve_digital_signature_algorithm))
