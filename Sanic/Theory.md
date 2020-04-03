In interpreter:

import sanic

dir(sanic.response) # List of functions for use

app = sanic.Sanic()
help(app.run) # To check possible parameters


# Request parameters properties list

'app', 'args', 'body', 'body_finish', 'body_init', 'body_push', 'content_type', 'cookies', 'ctx', 'endpoint', 'files', 'form', 'forwarded', 'get', 'get_args', 'get_query_args', 'headers', 'host', 'ip', 'json', 'load_json', 'match_info', 'method', 'parsed_args', 'parsed_files', 'parsed_form', 'parsed_forwarded', 'parsed_json', 'parsed_not_grouped_args', 'path', 'port', 'query_args', 'query_string', 'raw_args', 'raw_url', 'remote_addr', 'scheme', 'server_name',
'server_port', 'socket', 'stream', 'token', 'transport', 'uri_template', 'url', 'url_for', 'version'

# Websocket

- Do not name your file websocket.py, otherwise, you will not be able to
  import websocket-client module via 'import websocket'

  >>> import websocket
  >>> ws = websocket.WebSocket()
  >>> ws.connect('ws://localhost:8080/wsendpoint')
  >>> ws.status
  101
  >>> ws.recv()
  'Welcome to the sanic endpoint'
  >>> ws.send('Thank you for welcoming me')
  32
  >>>
  Server: The response from the client was: Thank you for welcoming me
