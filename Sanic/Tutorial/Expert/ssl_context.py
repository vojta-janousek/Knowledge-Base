import ssl
import sanic


app = sanic.Sanic()

context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(r'<path to certificace>', keyfile=r'path to keyfile')

@app.route('/')
async def index(request):
    return sanic.response.text('ok')


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=443, ssl=context)
