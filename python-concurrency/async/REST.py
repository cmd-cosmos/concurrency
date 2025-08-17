### REST API using the aiohttp framework

from aiohttp import web
import asyncio
import json

async def handle(request):
    '''
    Request Handler:
    Returns a response object.
    '''
    response_object = {
        'status' : 'success'
    }
    return web.Response(text=json.dumps(response_object), status=200)

async def new_user(request):
    try:
        user = request.query['name']
        print('creating a new user: {}'.format(user))

        response_object = {
            'status' : 'success',
            'message' : 'user created'
        }
        return web.Response(text=json.dumps(response_object), status=200)
    except Exception as e:
        response_object = {
            'status' : 'failure',
            'message' : str(e)
        }
        return web.Response(json.dumps(response_object), status=500)

app = web.Application()
app.router.add_get('/',handle)
app.router.add_post('/',new_user)

web.run_app(app=app)