#!/usr/bin/env python3
"""
task_03_http_server.py

Simple HTTP API using Python's built-in http.server module.

Endpoints:
- GET /         → "Hello, this is a simple API!"
- GET /data     → JSON with user info
- GET /status   → "OK"
- GET /info     → JSON with API metadata
- All others    → JSON 404 error
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_json(self, status_code, data):
        """Send a JSON response with proper headers."""
        response = json.dumps(data, indent=2).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def _send_text(self, status_code, text):
        """Send a plain text response."""
        response = text.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def do_GET(self):
        """Handle GET requests for specific endpoints."""
        routes = {
            "/": lambda: self._send_text(200, "Hello, this is a simple API!"),
            "/data": lambda: self._send_json(200, {
                "name": "John",
                "age": 30,
                "city": "New York"
            }),
            "/status": lambda: self._send_text(200, "OK"),
            "/info": lambda: self._send_json(200, {
                "version": "1.0",
                "description": "A simple API built with http.server"
            })
        }

        handler = routes.get(self.path)
        if handler:
            handler()
        else:
            self._send_json(404, {"error": "Endpoint not found"})

    def do_POST(self):
        """Reject all POST requests with 405 Method Not Allowed."""
        self._send_text(405, "Method Not Allowed")


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    """Start the HTTP server on port 8000."""
    port = 8000
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print("Server started on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
