conn = await connect(
    host='db',
    port=3306,
    user='user',
    password='password',
    db='db',
    loop=loop
)
db_cursor = await conn.cursor()

await db_cursor.execute('SELECT * FROM links')
qs = await db_cursor.fetchall()
data = dumps(qs)

await db_cursor.close()
conn.close()

return json(data, status=200)



@app.route('/<link_endpoint>')
async def redirect_link(request, link_endpoint):
    try:
        loop = get_event_loop()
        pool = await create_pool(
            host='db',
            port=3306,
            user='user',
            password='password',
            db='db',
            loop=loop
        )
        async with pool.acquire() as conn:
            db_cursor = await conn.cursor()

            query = 'SELECT * FROM links WHERE endpoint = %s'
            value = (link_endpoint,)
            await db_cursor.execute(query, value)
            result = await db_cursor.fetchall()

            url = result[0][1]
            return response.redirect(url)

    except Exception as error:
        print(error)
        return json({'message': 'link does not exist'}, status=400)


# query = await conn.execute(
#     table.select().where(endpoint=='vlk')
# )
# url = await query.fetchone()
# return json({'message': 'getting url successful'}, status=200)
# async with pool.acquire() as conn:
#     db_cursor = await conn.cursor()
#
#     query = 'SELECT * FROM links WHERE endpoint = %s'
#     value = (link_endpoint,)
#     await db_cursor.execute(query, value)
#     result = await db_cursor.fetchall()
#
#     url = result[0][1]
#     return response.redirect(url)
