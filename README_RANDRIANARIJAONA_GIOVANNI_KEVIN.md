# Travaux sur les Chaînes de Markov – Exercices & Mini-Projet

## Installation

```bash
# Entrer dans le dossier 
cd exercice_mini_projet

```bash
# Création de l'environnement virtuel
python -m venv .venv

# Activation de l'environnement virtuel
# Pour Windows
.venv\Scripts\activate
# Pour Linux/macOS
# source .venv/bin/activate

# Installation des dépendances
pip install -r requirements.txt
```

## Exécution des scripts

Après avoir activé l'environnement virtuel et installé les dépendances, vous pouvez exécuter les scripts :

### Exécuter les exercices

```bash
python -m scripts.run_exercises
```

### Exécuter la simulation M/M/1

```bash
python -m scripts.run_mm1
```

Les images des graphiques générées par cette simulation se trouveront dans le dossier `data/figures`.

## Dépannage

### ModuleNotFoundError: No module named 'src' ou 'utils'

Si vous rencontrez des erreurs `ModuleNotFoundError`, assurez-vous que vous exécutez les scripts en tant que modules Python depuis la racine du projet, comme indiqué ci-dessus.

### ModuleNotFoundError: No module named 'numpy' (ou autre bibliothèque)

Assurez-vous que toutes les dépendances sont installées en exécutant `pip install -r requirements.txt` après avoir activé l'environnement virtuel.

### Erreur de nom de fichier (ex: mm1_queu_sim.py)

Vérifiez que les noms de fichiers correspondent exactement aux importations dans le code. Par exemple, `mm1_queu_sim.py` a été renommé en `mm1_queue_sim.py` pour correspondre à l'importation `mm1_queue_sim`.
