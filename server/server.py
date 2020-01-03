import http.server
import socketserver

PORT = 80

Handler = http.server.CGIHTTPRequestHandler


class ModifiedCGI(Handler):
    def __init__(self):
        super()
        self.allowed = ("/", "/index.html")
        

    def do_GET(self):
        print(self.allowed)
        super().do_GET()
        return

if __name__ == "__main__":
    with http.server.HTTPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()
            print("\nStopping Server")
