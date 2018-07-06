import json

from flask import make_response
from flask_restful import Resource


class Ping(Resource):
    def get(self):
        resp = make_response(json.dumps({"dsad": "das"}))
        resp.set_cookie('username', '{"vitthal": "sarode"}')
        return resp
