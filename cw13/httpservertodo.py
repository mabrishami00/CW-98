from http.server import HTTPServer, BaseHTTPRequestHandler
import json

HOST = "127.0.0.1"
PORT = 9999

raw_data = {"id": 1, "title": "Read Book", "description": "Read shoedog book"}


todo = []


class ToDo(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        content = json.dumps(todo).encode("utf-8")
        self.wfile.write(content)

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        data_json = json.dumps(raw_data).encode("utf-8")
        todo.append(raw_data)
        self.wfile.write(data_json)


server = HTTPServer((HOST, PORT), ToDo)
print("server now running...")
server.serve_forever()
server.server_close()
print("server closed!")
