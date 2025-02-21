#!/usr/bin/python3
import requests
import json
import csv


def fetch_and_print_posts():
    """Récupère et affiche les titres
    des publications depuis une API."""
    """Envoie une requête GET à l'URL
    donnée pour récupérer les publications."""
    reponse = requests.get("https://jsonplaceholder.typicode.com/posts")

    """Vérifie si la requête a réussi (code de statut 200)."""
    if reponse.status_code == 200:
        print(reponse.status_code)
        reponse_json = reponse.json()

        """Parcourt chaque publication dans le JSON récupéré."""
        for _title in reponse_json:
            print(_title["title"])


def fetch_and_save_posts():
    """Récupère les publications depuis
    une API et les enregistre dans un fichier CSV."""
    """Envoie une requête GET à l'URL
    donnée pour récupérer les publications."""
    reponse = requests.get("https://jsonplaceholder.typicode.com/posts")

    """Vérifie si la requête a réussi (code de statut 200)."""
    if reponse.status_code == 200:
        print("Requête réussie !")
        reponse_json = reponse.json()
        posts_data = []

        """Parcourt chaque publication dans le JSON récupéré."""
        for add in reponse_json:
            """Ajoute un dictionnaire contenant les informations."""
            posts_data.append({
                "id": add["id"],
                "title": add["title"],
                "body": add["body"]
            })

        """Ouvre un fichier CSV en mode écriture."""
        with open('posts.csv', 'w', newline='', encoding='utf-8') as file_date:
            """Crée un écrivain pour le fichier
            CSV avec les noms des colonnes."""
            writer = csv.DictWriter(
                file_date, fieldnames=["id", "title", "body"]
            )
            writer.writeheader()

            """Parcourt chaque publication et l'écrit dans le fichier CSV."""
            for post in posts_data:
                writer.writerow(post)
