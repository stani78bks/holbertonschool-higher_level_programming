#!/usr/bin/python3
"""Defines function that fetches posts"""
import http.server
import json
import socketserver

"""
Script de serveur HTTP simple

Ce script définit un serveur HTTP simple qui gère
les requêtes GET pour différents points de terminaison.
Il utilise les modules `http.server` et `socketserver`
de la bibliothèque standard de Python.

Points de terminaison :
- GET / : Renvoie un message de salutation en texte brut.
- GET /data : Renvoie un objet JSON avec
des données d'exemple (nom, âge, ville).
- GET /status : Renvoie une réponse en texte
brut indiquant le statut du serveur (OK).
- Tout autre chemin : Renvoie une erreur 404 avec un message
indiquant que le point de terminaison n'a pas été trouvé.

Pour exécuter le serveur, lancez le script, et il écoutera sur le port 8000.
"""


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            dict_data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(dict_data)
            self.wfile.write(json_data.encode('utf-8'))

        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    PORT = 8000
    with socketserver.TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
        print(f"Serving at port {PORT}")
        httpd.serve_forever()
