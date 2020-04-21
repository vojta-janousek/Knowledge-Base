# @app.route('/', methods=['GET'])
# async def get_active_links(request):
#     try:
#         async with app.engine.acquire() as conn:
#             data = []
#             queryset = await conn.execute(actives.select())
#             for row in await queryset.fetchall():
#                 data.append((row.endpoint, row.owner, row.url))
#
#             return html(
#                 template_generators.all_links_page_generator(data),
#                 status=200
#             )
#
#     except Exception as error:
#         print(error)
#         return json({'message': 'getting links failed'}, status=500)


# @app.route('/my_links', methods=['GET'])
# @login_required
# async def owner_specific_links(request, user):
#     try:
#         async with app.engine.acquire() as conn:
#             ac_data, in_data = [], []
#             ac_queryset = await conn.execute(
#                 actives.select().where(
#                     actives.columns['owner_id'] == user.id
#                 )
#             )
#             in_queryset = await conn.execute(
#                 inactives.select().where(
#                     inactives.columns['owner_id'] == user.id
#                 )
#             )
#             for row in await ac_queryset.fetchall():
#                 ac_data.append((row.endpoint, row.url))
#
#             for row in await in_queryset.fetchall():
#                 in_data.append((row.endpoint, row.url))
#
#             return html(
#                 template_generators.my_links_page_generator(ac_data, in_data),
#                 status=200
#             )
#
#     except Exception as error:
#         print(error)
#         return json({'message': 'getting your links failed'}, status=500)
