from wsgiref.simple_server import make_server
from cgi import parse_qs, escape
import json
import gamedriver

def application(environ, start_response):
    response = {'code': 'error', 'msg': 'wrong HTTP method'}
    path = environ['PATH_INFO'].split('/')
    method = path[1]
    if method == 'new':
        response = gamedriver.new_game()
    elif method == 'guess':
        d = parse_qs(environ["QUERY_STRING"])
        guess = escape(d.get('guess', [''])[0])
        guess = int(guess)
        response = gamedriver.guess(d)
    else:
        response = {'code': 'error', 'msg': 'non-existent API method'}

    status = '200 OK'
    response_body = json.dumps(response)
    response_headers = [
        ('Content-Type', 'application/json'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)
    return [response_body]

httpd = make_server('localhost', 'Port', application)
httpd.serve_forever()