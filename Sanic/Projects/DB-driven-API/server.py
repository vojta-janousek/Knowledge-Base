import mysql.connector

from sanic import Sanic
from sanic.response import json

from json import dumps


app = Sanic()

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='damsi80Rakvicek',
    database='cat_list'

)
mycursor = mydb.cursor()


@app.route('/create_cat', methods=['POST'])
async def create_cat(request):
    try:
        data = request.json

        query = 'INSERT INTO cat (id, name, age, weight) VALUES (%s, %s, %s, %s)'
        values = (data['id'], data['name'], data['age'], data['weight'])
        mycursor.execute(query, values)
        mydb.commit()

        return json({'message': 'cat creation successful'}, status=201)

    except Exception as error:
        print(error)
        return json({'message': 'cat creation failed'}, status=500)


@app.route('/get_cats', methods=['GET'])
async def get_cats(request):
    try:
        mycursor.execute('SELECT * FROM cat')
        qs = mycursor.fetchall()
        data = dumps(qs)
        return json(data, status=200)
    except Exception as error:
        print(error)
        return json({'message': 'getting cats failed'}, status=500)


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=8000)
