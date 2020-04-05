## Microservices

- Data are entered in the python/flask app, which talks to redis.
- Redis passes off the data to the .NET worker
- The worker writes the data to postgreSQL
- Results are passed to the express based node.JS app
