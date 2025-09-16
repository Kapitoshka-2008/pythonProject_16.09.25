from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
CONTACTS_FILE = PROJECT_ROOT / "contacts.html"


class ContactsOnlyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            with open(CONTACTS_FILE, "r", encoding="utf-8") as file:
                html_content = file.read()
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(html_content.encode("utf-8"))
        except FileNotFoundError:
            self.send_response(500)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("contacts.html not found".encode("utf-8"))

    def log_message(self, format, *args):
        return


def run(host: str = "127.0.0.1", port: int = 8000) -> None:
    server_address = (host, port)
    httpd = HTTPServer(server_address, ContactsOnlyHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()


if __name__ == "__main__":
    run()


