# Minitrice

Petit projet d’évaluation Git : une calculatrice en ligne de commande (`minitrice`) et un générateur d’expressions aléatoires (`generator`). Le dépôt fournit aussi des jeux de tests et les résultats attendus.

## Table des matières
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Exécution](#exécution)
- [Résultats fournis](#résultats-fournis)
- [Remarques](#remarques)
- [Publication](#publication)
- [Références/Liens utiles](#référencesliens-utiles)

## Prérequis
- Python 3.10 ou plus récent (interpréteur CPython testé sous macOS/Linux).
- Accès à un terminal POSIX pour lancer les exécutables.

## Installation
1. Cloner ce dépôt et placer-vous à sa racine.
2. (Optionnel) Créer un environnement virtuel :
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Aucune dépendance externe n’est requise : les scripts utilisent uniquement la bibliothèque standard.
4. Rendre les scripts exécutables si besoin :
   ```bash
   chmod +x minitrice generator
   ```

## Exécution
### Mode interactif
```bash
./minitrice
> 3+9
12
> 12/5
2.4
> \u0004
Fin des calculs
```

### Lecture depuis STDIN
```bash
echo "3+12" | ./minitrice
# => 15
cat good-expression.txt | ./minitrice
```

### Génération aléatoire + calcul
```bash
./generator 5 | ./minitrice
```
`generator` produit des expressions valides composées de deux entiers positifs compris entre 1 et 1000 et d’une opération parmi `+ - * /`.

## Résultats fournis
Le dossier `test/` contient trois jeux d’entrées (`00-addition.txt`, `01-subtraction.txt`, `02-mixed.txt`).
Les fichiers correspondants dans `results/` sont générés via `cat test/<fichier> | ./minitrice > results/<fichier>-result.txt`. Ils servent de référence pour vérifier le comportement du programme.

## Remarques
- Parsing basé sur une expression régulière stricte : toute ligne qui ne correspond pas à `nombre opérateur nombre` renvoie `Erreur de syntaxe...` avec un code de sortie `1`.
- Les résultats sont arrondis à deux décimales quand nécessaire et simplifiés si la partie décimale est nulle.
- Le projet est pensé pour suivre GitFlow : toute nouvelle fonctionnalité passe par `feature/<nom>` puis merge vers `main` lorsque la fonctionnalité est stable.

## Publication
Option bonus : visualiser l’historique avec Gource puis encoder la vidéo avec `ffmpeg`.
```bash
gource -s 2 -r 60 --file-font-size 8 --title git-evaluation \
  --filename-time 2 --stop-at-end --hide date,usernames -o video.ppm
ffmpeg -y -r 60 -f image2pipe -vcodec ppm -i video.ppm \
  -vcodec libx264 -preset medium -pix_fmt yuv420p -crf 18 video.mp4
```
Publiez ensuite `video.mp4` sur YouTube et mentionnez le lien ici.

## Références/Liens utiles
- Cours Git ESGI & workflow GitFlow (documentation du module).
- [A successful Git branching model](https://nvie.com/posts/a-successful-git-branching-model/)
- [Philosophie Unix — Wikipédia](https://fr.wikipedia.org/wiki/Philosophie_Unix)
