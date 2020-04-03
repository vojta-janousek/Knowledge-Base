import sanic


app = sanic.Sanic()
# app = sanic.Sanic('LoggingDemo', debug_log=True, access_log=False)


@app.route('/')
async def index(request):
    return sanic.response.text('ok')


if (__name__ == '__main__'):
    LOGGING_CONFIG = {
        'debug_log': True,
        'access_log': False
    }
    app.run(host='0.0.0.0', port=8080, log_config= LOGGING_CONFIG)
    # app.run(host='0.0.0.0', port=8080, debug_log=True, access_log=False)
