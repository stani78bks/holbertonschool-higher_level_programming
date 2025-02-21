#!/usr/bin/python3
import requests  # bibliothèque requestspour faire des requêtes HTTP
import json      # bibliothèque json pour manipuler des données JSON
import csv       # bibliothèque csv pour travailler avec des fichiers CSV


def fetch_and_print_posts():
    """Récupère et affiche les titres des publications depuis une API."""
    # Envoie une requête GET à l'URL donnée pour récupérer les publications
    reponse = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Vérifie si la requête a réussi (code de statut 200)
    if reponse.status_code == 200:
        print(reponse.status_code)  # Affiche le code de statut de la réponse
        reponse_json = reponse.json()  # Convertit la réponse en objet JSON

        # Parcourt chaque publication dans le JSON récupéré
        for _title in reponse_json:
            print(_title["title"])  # Affiche le titre de chaque publication


def fetch_and_save_posts():
    """Récupère les publications depuis une
    API et les enregistre dans un fichier CSV."""
    # Envoie une requête GET à l'URL donnée pour récupérer les publications
    reponse = requests.get("https://jsonplaceholder.typicode.com/posts")

    # Vérifie si la requête a réussi (code de statut 200)
    if reponse.status_code == 200:
        print("Requête réussie !")  # Affiche un message de succès
        reponse_json = reponse.json()  # Convertit la réponse en objet JSON
        posts_data = []  # Initialise une liste pour stocker les données

        # Parcourt chaque publication dans le JSON récupéré
        for add in reponse_json:
            # Ajoute un dictionnaire contenant les informations
            posts_data.append({
                "id": add["id"],    # Récupère l'identifiant de la publication
                "title": add["title"],  # Récupère le titre de la publication
                "body": add["body"]     # Récupère le contenu de la publication
            })

        # Ouvre un fichier CSV en mode écriture
        with open('posts.csv', 'w', newline='', encoding='utf-8') as file_date:
            # Crée un écrivain pour le fichier CSV avec les noms des colonnes
            writer = csv.DictWriter(
                file_date, fieldnames=["id", "title", "body"]
            )
            writer.writeheader()  # Écrit les en-têtes dans le fichier CSV

            # Parcourt chaque publication et l'écrit dans le fichier CSV
            for post in posts_data:
                writer.writerow(post)  # Écrit la ligne de données
