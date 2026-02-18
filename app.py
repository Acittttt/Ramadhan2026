from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
        # Baca konten file index.html
        try:
            with open('index.html', 'r', encoding='utf-8') as file:
                content = file.read()
            self.wfile.write(bytes(content, "utf8"))
        except FileNotFoundError:
            # Fallback jika index.html tidak ditemukan
            message = "<h1>Halo Cloud!</h1><p>Server ini dikonfigurasi oleh: KoTA-108</p>"
            self.wfile.write(bytes(message, "utf8"))

def run():
    print('Mulai server...')
    server_address = ('0.0.0.0', 8080)
    httpd = HTTPServer(server_address, SimpleHandler)
    print('Server berjalan di port 8080...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
