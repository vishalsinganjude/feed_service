
from flask_restful import Resource
from flask import request, jsonify


from feed_service.service_apis_handler.notification_get_handler import get_Notification_By_UserId
from feed_service.service_apis_handler.notification_put_handle import read_all_notification
from feed_service.services import user_service
from feed_service.utils import get_Notification_by_response_dict



class Notification(Resource):
    def get(self):
        auth_token = request.cookies.get('auth_key')
        is_valid, user_object = user_service.validate_and_get_user(auth_token)

        #//check  of unautherize access

        Notification_object = get_Notification_By_UserId(user_object)
        # for x in Notification_object:
            # print "###########################"
            # print "Notification Object(Get) ----->", Notification_object
            # print "###########################"
        # print Notification_object
        response_dict = get_Notification_by_response_dict.get_Notification_by_response_dict(Notification_object)
        # print response_dict
        return jsonify({"notification":response_dict})

    def put(self):
        auth_token = request.cookies.get('auth_key')
        is_valid, user_object = user_service.validate_and_get_user(auth_token)
        Notification_object = get_Notification_By_UserId(user_object)
        print "###########################"
        print "Notification Object(put) ----->", Notification_object
        print "###########################"

        Notification_read = read_all_notification(Notification_object)


        return None
