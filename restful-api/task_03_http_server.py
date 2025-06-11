#!/usr/bin/env python3
"""
task_03_http_server.py

A basic HTTP API using Python's built-in http.server module.

Endpoints:
- GET /         → "Hello, this is a simple API!"
- GET /data     → JSON with user info
- GET /status   → "OK"
- GET /info     → JSON with API metadata
- All others    → JSON 404 error

Run the server with:
    python3 task_03_http_server.py
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_json(self, status_code, data):
        """Helper to send a JSON response."""
        response = json.dumps(data).encode()
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def _send_text(self, status_code, text):
        """Helper to send a plain text response."""
        response = text.encode()
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def do_GET(self):
        """Handle GET requests for predefined endpoints."""
        if self.path == "/":
            self._send_text(200, "Hello, this is a simple API!")

        elif self.path == "/data":
            self._send_json(200, {
                "name": "John",
                "age": 30,
                "city": "New York"
            })

        elif self.path == "/status":
            self._send_text(200, "OK")

        elif self.path == "/info":
            self._send_json(200, {
                "version": "1.0",
                "description": "A simple API built with http.server"
            })

        else:
            self._send_json(404, {"error": "Endpoint not found"})


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    """Start the HTTP server on port 8000."""
    port = 8000
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"✅ Server running at http://localhost:{port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
