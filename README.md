# setup_logicom
Ce programme est un outil d'automatisation conçu pour installer et configurer automatiquement les logiciels de Logicom sur votre ordinateur. Il simplifie le processus d'installation en effectuant toutes les étapes nécessaires pour configurer les logiciels selon les paramètres pré-définis, vous faisant gagner du temps et réduisant les erreurs humaines.

## Description

Le programme réalise les tâches suivantes :
- **Télécharge les logiciels nécessaires** : Il récupère les logiciels de Logicom à partir de sources définies.
- **Installe les logiciels** : Il exécute les installations en utilisant des paramètres d'installation automatisés pour chaque logiciel.
- **Configure les logiciels** : Il applique des configurations par défaut ou personnalisées pour chaque logiciel afin qu'ils soient prêts à l'emploi dès la fin de l'installation.
- **Gère les dépendances** : Il s'assure que toutes les bibliothèques et outils nécessaires sont installés et configurés correctement.


## Prérequis

Pour exécuter ce programme, vous devez avoir Python installé sur votre ordinateur. Il est recommandé d'utiliser une version 32 bits de Python.

## Installation

1. **Téléchargez et installez Python** (version 32 bits recommandée) depuis le site officiel [python.org](https://www.python.org/downloads/).

2. **Installez les bibliothèques nécessaires en utilisant pip**
Exécutez la commande suivante :
pip install pyautogui 

meme pour : pywinauto et pyuac

3. **Utilisation**
Pour exécuter le programme et commencer l'installation et la configuration des logiciels, utilisez la commande suivante :
python logicom.py
python logicom2.py 

**NB** : le dossier installation que j'ai envoyé par we transfer doit etre mis en D: 