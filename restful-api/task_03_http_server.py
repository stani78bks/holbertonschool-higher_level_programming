#!/usr/bin/env python3
"""
task_03_http_server.py

A basic HTTP API using Python's built-in http.server module.

Endpoints:
- GET /         → Simple welcome message
- GET /data     → JSON: {"name": "John", "age": 30, "city": "New York"}
- GET /status   → "OK"
- GET /info     → JSON with API version and description
- All others    → JSON 404 error

Usage:
Run the server with: python3 task_03_http_server.py
Then visit: http://localhost:8000/ in your browser or use curl.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json

class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests and route them to the correct endpoint."""
        # Root endpoint
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # /data returns JSON data
        elif self.path == "/data":
            response = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        # /status returns plain OK
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # /info returns API metadata
        elif self.path == "/info":
            response = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

        # Unknown endpoint → 404 Not Found
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_message = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_message).encode())

def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    """Start the HTTP server."""
    port = 8000
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"🚀 Server running at http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
