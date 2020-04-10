'''
Copyright (C) 2020 Link Shortener Authors
Licensed under the MIT (Expat) License. See the LICENSE file found in the
top-level directory of this distribution.
'''
from asyncio import get_event_loop

from aiomysql import create_pool
from aiomysql.sa import create_engine

from sqlalchemy import MetaData, Table, Column, String, Integer, Text
from sqlalchemy.sql import select
# from sqlalchemy.sql.expression import insert
from sqlalchemy.schema import CreateTable

from json import dumps

from sanic import Sanic, response
from sanic.response import json

from blueprint_test import bp


app = Sanic(__name__)
app.blueprint(bp)

metadata = MetaData()
table = Table(
    'links',
    metadata,
    Column('endpoint', String(30)),
    Column('url', String(250))
)


@app.listener('before_server_start')
async def initialise_db(app, loop):
    global engine
    engine = await create_engine(
        host='db',
        port=3306,
        user='user',
        password='password',
        db='db',
        loop=loop
    )
    async with engine.acquire() as conn:
        await conn.execute(CreateTable(table))

        await conn.execute(
            table.insert().values(endpoint='vlk', url='www.vlk.cz')
        )

        # await conn.close()


@app.route('/api/links', methods=['GET'])
async def get_links(request):
    try:
        # loop = get_event_loop()
        global engine
        async with engine.acquire() as conn:
            data = []
            queryset = await conn.execute(table.select())
            for row in await queryset.fetchall():
                data.append({
                    'endpoint': row.endpoint,
                    'url': row.url
                })

            # await conn.close()
            return json(dumps(data), status=200)

    except Exception as error:
        print(error)
        return json({'message': 'getting links failed'}, status=500)


@app.route('/<link_endpoint>')
async def redirect_link(request, link_endpoint):
    try:
        # loop = get_event_loop()
        global engine
        async with engine.acquire() as conn:
            sel = select([table]).where(
                table.columns['endpoint'] == link_endpoint
            )
            query = await conn.execute(sel)
            url = await query.fetchone()

            # await conn.close()
            return response.redirect(url[1])

    except Exception as error:
        print(error)
        return json({'message': 'link does not exist'}, status=400)


if (__name__ == '__main__'):
    app.run(host='0.0.0.0', port=8000)
