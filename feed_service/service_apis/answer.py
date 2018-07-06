from flask import request, jsonify
from flask_restful import Resource

from feed_service.service_apis_handler import answer_post_handler, \
    answer_get_handler
from feed_service.service_apis_handler.NotificationHandler import create_Notification_Object
from feed_service.service_apis_handler.answer_get_handler import get_answer_for_question
from feed_service.services import user_service
from feed_service.utils import answer_utils


class Answer(Resource):
    def post(self):
        # import pdb;
        # pdb.set_trace()
        auth_token = request.cookies.get('auth_key')
        # print auth_token
        is_valid, user_object = user_service.validate_and_get_user(auth_token)
        print user_object

        username = user_object['username']
        # print username

        if not is_valid:
            return {"success": False, "message": "Invalid User !!"}, 401
        # print user_object

        request_data = request.get_json()
        # print request_data
        answer_object = answer_post_handler.create_answer(request_data, username)
        response_dict = answer_utils.get_answer_dict(answer_object)

        ###########Notification ##########
        action_by = username
        owner_by = answer_object.question.user_id
        entity_id = answer_object.question.id
        entity_type="Answer"

        # print "============================="
        # print action_by, owner_by, entity_id, entity_type
        # print "============================="

        Notification = create_Notification_Object(entity_type,entity_id, action_by, owner_by)

        if Notification :

            return jsonify({"answer": response_dict})

    def get(self, questionId=None):
        if questionId:
            answer_object = answer_get_handler.get_answer_for_question(questionId)

            if answer_object:
                return jsonify({"Answer": get_answer_for_question(questionId)})

            else:
                return {"success": False}
        # request_data = request.args
        #
        # if "questionId" in request_data:
        #     answer_object = answer_get_handler.get_answer_for_question(request_data["questionId"])
        else:
            answer_object = answer_get_handler.get_all_answer()

        answer_objects = [answer_utils.get_answer_dict(x) for x in answer_object]
        return jsonify({"answers": answer_objects})
