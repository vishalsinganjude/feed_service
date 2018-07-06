from flask import request, jsonify
from flask_restful import Resource

from feed_service.service_apis_handler import downvote_post_handler, answer_get_handler
from feed_service.service_apis_handler.NotificationHandler import create_Notification_Object
from feed_service.services import user_service
from feed_service.utils import downvote_utils


class Downvote(Resource):
    def post(self):
        request_data = request.get_json()
        downvote_object = downvote_post_handler.create_downvote(request_data)
        response_dict = downvote_utils.get_downvote_dict(downvote_object)

        auth_token = request.cookies.get('auth_key')

        is_valid, user_object = user_service.validate_and_get_user(auth_token)
        username = user_object['username']
        answer_id = request_data['answerId']
        answer_object = answer_get_handler.get_answer_by_id(answer_id)

        # print "#######################################################################"
        # print "Action By============================>",username
        # print "Owner By============================>",answer_object.user_id
        # print "Entity Id============================>",answer_object.id
        # print "entity_type============================> Downvote"
        # print "#######################################################################"

        entity_type = "Downvote"
        entity_id = answer_object.id
        action_by = username
        owner_by = answer_object.user_id

        Notification = create_Notification_Object(entity_type, entity_id, action_by, owner_by)

        if Notification:
            return jsonify({"Downvote": response_dict})
