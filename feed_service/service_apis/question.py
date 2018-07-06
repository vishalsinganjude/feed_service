from flask import session, request, jsonify
from flask.json import jsonify
from flask_restful import Resource

from feed_service.service_apis_handler import question_post_handler, question_get_handler
from feed_service.utils import question_utils


class Question(Resource):
    def post(self):
        # read the auth token from cookie
        # request the auth token to user_service and get asociated user
        # if token is invalid return respose unauthorised
        # if token is valid then follow the step
        # import pdb; pdb.set_trace()
        # print session
        auth_token = request.cookies.get('auth_key')
        # print "Auth-token=>", auth_token
        # is_valid, user_object = user_service.validate_and_get_user(auth_token)
        #
        # if not is_valid:
        # return {"success": False, "message": "Invalid User !!"}, 401

        if session['key'] != auth_token:
            return {"success": False, "message": "Invalid User !!"}

        request_data = request.get_json()
        username = session['username']

        result = question_post_handler.create_question(request_data, username)
        if result:
            response_dict = question_utils.get_question_dict(result)
            return jsonify({"question": response_dict})
        else:
            return {"success": False}

    def get(self, user_id=None):
        if user_id:
            question_objects = question_get_handler.get_question_for_user(user_id)
        else:
            question_objects = question_get_handler.get_all_questions()

            response_dicts = [question_utils.get_question_dict(x) for x in question_objects]
            return jsonify({"questions": response_dicts})
