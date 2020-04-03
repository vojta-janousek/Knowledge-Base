import sanic


app = sanic.Sanic('my_app')

# $ MYAPP_SETTINGS=/Users/vojta/Documents/GitHub/Knowledge-Base
#   /Sanic/Advanced/app.conf python loading_configuration.py
app.config.from_envvar('MYAPP_SETTINGS')


@app.route('/<param>')
async def index(request, param):
    return sanic.response.text(
        'The value of {} is {}'.format(param, app.config.get(param, 'default'))
        )


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=8080)
