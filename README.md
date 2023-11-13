# String Art
![Language](https://img.shields.io/badge/Language-Python-f2cb1b)
<br/>

Projet de conversion d'image en String Art.

<br/>

<div style="display: flex; align-items: center;">
    <img src="https://i.imgur.com/IZZSufN.png" style="width: 50%;">
</div>



<br/>


## Explications

L'objectif est d'implémenter plusieurs algorithmes et comparer les résultats.
Il y a deux algorithmes (et demi), le premier étant basé sur le projet de grvlbit, tandis que le deuxième est un algorithme glouton avec une représentation plus précise des lignes par rapport à l'algorithme 1. Cependant, il est fortement inefficace (O(nb_pixel * nb_clous * nb_fil)). La version 2.5 améliore le temps de calcul en simplifiant la représentation des lignes en réutilisant l'algorithme glouton de l'algorithme 2 et l'algorithme de Bresenham de l'algorithme 1.

L'algorithme 1 propose de bons résultats pour un grand nombre de clous/fils (~600/ ~3000) en un temps correct (~10 secondes), tandis que l'algorithme 2 prendra beaucoup trop de temps et l'algorithme 2.5 prendra un temps de l'ordre de la minute.

Pour des rendus avec beaucoup de fils/clous, il est préférable de prendre l'algorithme 1, tandis que l'algorithme 2.5 sera bien meilleur pour des rendus avec moins de clous/fils (~100/ ~300).

## Axes d'amélioration

- Faire une meilleure version de l'algorithme de prétraitement (qui est, selon moi, vraiment pas optimal pour l'instant).
- Implémenter une version 3 basée sur la FFT (théoriquement beaucoup plus efficace).

## Le programme

    python __main__.py -s "<nom_de_l'image>" -c <nb_de_clous> -f <nb_de_fils>

Si les options ne sont pas renseignées, alors les options par défaut seront utilisées. De plus, les valeurs de `self.weight` pour l'algorithme 1 et de `self.poids` pour les algorithmes 2 et 2.5 peuvent être modifiées pour obtenir différents résultats. Pour changer d'algorithme, il faut changer le nom de la fonction appelée dans le main à la ligne 84 :

- Algorithme 1 : `generator.generate()`
- Algorithme 2 : `generator.generate_v2()`
- Algorithme 2.5 : `generator.generate_v2_5()`

## Source

Basé initialement sur le projet de grvlbit : https://github.com/grvlbit/stringart
