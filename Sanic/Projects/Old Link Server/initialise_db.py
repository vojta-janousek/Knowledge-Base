'''
Copyright (C) 2020 Link Shortener Authors
Licensed under the MIT (Expat) License. See the LICENSE file found in the
top-level directory of this distribution.


Creates and populates a new table with links and their endpoints.
'''
import asyncio
import aiomysql


async def initialise_database():
    conn = await aiomysql.connect(
        host='db',
        port=3306,
        user='user',
        password='password',
        db='db',
        loop=loop
    )
    db_cursor = await conn.cursor()
    await db_cursor.execute(
        'CREATE TABLE IF NOT EXISTS links (endpoint TEXT, url TEXT)'
    )
    query = 'INSERT INTO links (endpoint, url) VALUES (%s, %s)'
    data = [
        ('google', 'https://www.google.com/'),
        ('pomuzemesi', 'https://staging.pomuzeme.si'),
        ('epark', 'https://www.eparkomat.com/app/'),
        ('vlk', 'http://www.vlk.cz'),
        ('kodex', 'https://github.com/Applifting/culture'),
        ('meta', 'https://github.com/Applifting/link-shortener')
    ]
    await db_cursor.executemany(query, data)
    await conn.commit()

    await db_cursor.close()
    conn.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(initialise_database())


# @initdb_blueprint.listener('before_server_start')
# async def initialise_db(app, loop):
#     pool = await create_pool(
#         host='db',
#         port=3306,
#         user='user',
#         password='password',
#         db='db',
#         loop=loop,
#         autocommit=True
#     )
#     app.engine = await create_engine(
#         host='db',
#         port=3306,
#         user='user',
#         password='password',
#         db='db',
#         loop=loop
#     )
#     async with pool.acquire() as conn:
#         db_cursor = await conn.cursor()
#         try:
#             await db_cursor.execute(
#                 str(CreateTable(initdb_blueprint.active_table))
#             )
#             await db_cursor.execute(
#                 str(CreateTable(initdb_blueprint.inactive_table))
#             )
#             await db_cursor.executemany(
#                 'INSERT INTO active_links (owner, owner_id, endpoint, url) \
#                  VALUES (%s, %s, %s, %s)',
#                 active_data
#             )
#             await db_cursor.executemany(
#                 'INSERT INTO inactive_links (owner, owner_id, endpoint, url) \
#                  VALUES (%s, %s, %s, %s)',
#                 inactive_data
#             )
#
#         except Exception as error:
#             print(str(error) + '\n' + 'Tables are probably already cached')
#
#         await db_cursor.close()
#
#     pool.terminate()
#     await pool.wait_closed()
