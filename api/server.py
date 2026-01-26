from http.server import BaseHTTPRequestHandler, HTTPServer
import base64
import json
from urllib.parse import urlparse

from routes_get import get_all_transactions, get_transaction_by_id


USERNAME = "admin"
PASSWORD = "admin123"


def check_auth(headers):
    auth = headers.get("Authorization")
    if not auth:
        return False

    try:
        method, encoded = auth.split()
        decoded = base64.b64decode(encoded).decode("utf-8")
        username, password = decoded.split(":")
        return username == USERNAME and password == PASSWORD
    except:
        return False


class RequestHandler(BaseHTTPRequestHandler):

    # ----------------------------------------
    # AUTH REQUIRED FOR ALL ENDPOINTS
    # ----------------------------------------
    def authenticate(self):
        if not check_auth(self.headers):
            self.send_response(401)
            self.send_header("WWW-Authenticate", "Basic realm='Access Denied'")
            self.end_headers()
            self.wfile.write(b"Unauthorized")
            return False
        return True

    # ----------------------------------------
    # GET REQUESTS
    # ----------------------------------------
    def do_GET(self):
        if not self.authenticate():
            return

        path = urlparse(self.path).path

        if path == "/transactions":
            status, data = get_all_transactions()
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(data.encode())
            return

        if path.startswith("/transactions/"):
            tx_id = path.split("/")[-1]
            status, data = get_transaction_by_id(tx_id)

            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(data.encode())
            return

        # Invalid route
        self.send_response(404)
        self.end_headers()
        self.wfile.write(b"Not Found")


def run_server():
    server_address = ("0.0.0.0", 8080)
    httpd = HTTPServer(server_address, RequestHandler)
    print("Server running on http://localhost:8080")
    httpd.serve_forever()


if __name__ == "__main__":
    run_server()

