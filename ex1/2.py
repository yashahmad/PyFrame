import urllib

def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/html; charset=utf-8')]
    start_response(status, headers)

    GET = urllib.parse.parse_qs(environ['QUERY_STRING'])
    name = GET.get('name', ['PyCon'])[0]

    return [(f'<h1>Hello {name}!</h1>').encode('utf-8')]
