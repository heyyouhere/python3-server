from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import json
import uni

class Handler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        j = uni.getNews()
        self.wfile.write(j.encode())


def run(server_class=HTTPServer, handler_class=Handler, port=8080):
	logging.basicConfig(level=logging.INFO)
	server_address = ('', port)
	httpd = server_class(server_address, handler_class)
	logging.info('Starting httpd...\n')
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	httpd.server_close()
	logging.info('Stopping httpd...\n')



if __name__ == '__main__':
	from sys import argv
	if len(argv) == 2:
		run(port=int(argv[1]))
	else:
		run(port = 502)
