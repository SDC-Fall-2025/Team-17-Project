import flask
import json

__all__ = ['App']

class App(object):
    def __init__(self, name=__name__, /):
        self.name = name
        self.ctx = {
            'name': 'SDC Team 17'
        }

    def greet(self):
        return 'Hello {0[name]}!'.format(self.ctx)

    def to_wsgi_app(self):
        app = flask.Flask(self.name)

        @app.route('/')
        def index():
            payload = json.dumps({'message': self.greet()})
            return flask.Response(payload, content_type='application_json')

        return app
