import falcon
from .example import Resource

api = application = falcon.API()

example = Resource()
api.add_route('/example', example)
api.add_route('/', example)
