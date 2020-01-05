import http.server
import socketserver
import os

PORT = 8000

Handler = http.server.CGIHTTPRequestHandler


class ModifiedCGI(Handler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.abspath(__file__)), **kwargs)
        

if __name__ == "__main__":
    with http.server.HTTPServer(("", PORT), ModifiedCGI) as httpd:
        print("serving at port", PORT)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()
            print("\nStopping Server")
