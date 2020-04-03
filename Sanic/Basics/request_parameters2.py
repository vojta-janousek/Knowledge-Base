import sanic


app = sanic.Sanic()


@app.route('/')
async def index(request):
    print(dir(request))
    return sanic.response.text('OK')


@app.route('/url')
async def index_url(request):
    return sanic.response.text('The url was: {}'.format(request.url))


@app.route('/query_string')
async def index_qstring(request):
    return sanic.response.text(
        'The url query was: {}'.format(request.query_string)
        )

if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=8080)
