Projet de conversion d'image en String Art.

L'objectif est d'implémenter plusieurs algos et comparer les résultats.
Il y a deux algos (et demis), le premier se basant sur le projet de grvlbit, 
le deuxième est un algo glouton avec une représentation plus décisive des lignes par rapport à l'algo 1.
Cependant il est fortement inefficace (O(nb_pixel*nb_clous*nb_fil)).
La version 2.5 améliore le temps de calcul en simplifiant la réprésentation des lignes en réutilisant l'algo glouton de l'algo 2 et l'algo de Bresenheim de l'algo 1.

L'algo 1 propose de bons résultats pour un grand nombre de clous/fils (~600/~3000) en un temps correct. (~10sec) tandis que l'algo 2 mettra beaucoup trop de temps et le 2.5
mettra un temps de l'ordre de la minute.

Pour des rendus avec beaucoup de fils/clous, il est préférable de prendre l'algo 1 tandis que l'algo 2.5 sera bien meilleur pour des rendus avec moins de clous/fils (~100/~300).

Axe d'amélioration : 
    -Faire une meilleure version de l'algo de Preprocessing (qui est selon moi vraiment pas ouf pour l'instant).
    -Implémenter une version 3 basé sur la FFT (théoriquement bien plus efficace).

Comment lancer le programme: 
    python __main__.py -s "<nom_de_l'image>" -c <nb_de_clou> -f <nb_de_fils>

    Si les options ne sont pas renseignés, alors les options par défaut seront utilisés.
    De plus, les valeurs de self.weight pour l'algo 1 et de self.poids pour les algos 2 et 2.5 peuvent être changé pour obtenir différents résultats.
    Pour changer d'algorithme, il faut changer le nom de fonction appelé dans le main ligne 84 : 
    Algo 1 : generator.generate() 
    Algo 2 : generator.generate_v2() 
    Algo 2.5 : generator.generate_v2_5() 

Basé initialement sur le projet de grvlbit : https://github.com/grvlbit/stringart


