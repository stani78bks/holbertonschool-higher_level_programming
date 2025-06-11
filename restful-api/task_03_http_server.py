#!/usr/bin/env python3
"""
task_03_http_server.py

Simple HTTP API using Python's built-in http.server module.
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_json(self, status_code, data):
        response = json.dumps(data).encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")  # ✅ no charset
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def _send_text(self, status_code, text):
        response = text.encode("utf-8")
        self.send_response(status_code)
        self.send_header("Content-Type", "text/plain")  # ✅ no charset
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)

    def do_GET(self):
        if self.path == "/":
            self._send_text(200, "Hello, this is a simple API!")  # ✅ message exact
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

    def do_POST(self):
        self._send_text(405, "Method Not Allowed")


def run():
    port = 8000
    server_address = ("", port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print("Server started on port 8000...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
