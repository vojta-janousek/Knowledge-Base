import sanic


app = sanic.Sanic()
#

@app.websocket('/wsendpoint')
async def endpoint_server(request, ws):
    while True:
        await ws.send('Welcome to the sanic endpoint')
        data = await ws.recv()
        print('The response from the client was: {}'.format(data))


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=8080)
