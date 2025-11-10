import flask
import json

from werkzeug.exceptions import HTTPException

__all__ = ['App']

class App(object):
    def __init__(self, name=__name__, /):
        self.name = name
        self.ctx = {
            'name': 'SDC Team 17'
        }

    def greet(self):
        return 'Hello {0[name]}!'.format(self.ctx)

    def search(self, params):
        # A very bad search function
        return [f"Hello from {__name__}",
                "No one has implemented me yet.",
                "Here are the params I got anyways:",
                params]

    def to_wsgi_app(self):
        app = flask.Flask(self.name)

        @app.route('/api/v1/greet')
        def index():
            payload = json.dumps({'message': self.greet(), 'ok': True})
            return flask.Response(payload, content_type='application/json')

        @app.errorhandler(HTTPException)
        def handle_http_exception(e):
            response = e.get_response()
            response.data = json.dumps({
                'ok': False,
                "error": e.name,
                "description": e.description,
                "code": e.code,
            })
            response.content_type = "application/json"
            return response

        @app.route('/api/v1/search', methods=['POST'])
        def search():
            if not flask.request.is_json:
                flask.abort(415, description='Need application/json')
            payload = json.dumps({'results': self.search(flask.request.json), 'ok': True})
            return flask.Response(payload, content_type='application/json')

        return app
