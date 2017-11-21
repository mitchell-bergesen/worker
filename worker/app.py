import falcon
from .example import Resource

api = application = falcon.API()

example = Resource()
api.add_route('/example', example)
api.add_route('/', example)

def getApp():
    """ This returns the application object (for use in auto-testing, for example) """
    return api