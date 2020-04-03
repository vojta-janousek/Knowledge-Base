# Strict slashes tell you how your urls should end
import sanic


# app = sanic.Sanic(strict_slashes=True)
app = sanic.Sanic()


@app.route('/', strict_slashes=False)
async def index(request):
    return sanic.response.text('Without strict slashes')


@app.route('/strict', strict_slashes=True)
async def index(request):
    return sanic.response.text('With strict slashes')


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=8080)
