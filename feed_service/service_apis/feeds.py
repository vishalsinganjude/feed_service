
from flask import jsonify
from flask_restful import Resource

from feed_service.service_apis_handler import feed_get_handler


class Feed(Resource):
    def get(self):
        response = feed_get_handler.get_feed_data()
        return jsonify({"questions":response})
