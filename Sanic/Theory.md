In interpreter:

import sanic

dir(sanic.response) # List of functions for use

app = sanic.Sanic()
help(app.run) # To check possible parameters
