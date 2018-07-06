from flask import request

from feed_service.db.feed_models.models import Downvote, Upvote
from feed_service.service_apis_handler import answer_get_handler
from feed_service.services import user_service
from feed_service.utils.exceptions import InternalServerError


def create_downvote(request_data):
    auth_token = request.cookies.get('auth_key')
    is_valid, user_object = user_service.validate_and_get_user(auth_token)
    username = user_object['username']
    answer_id = request_data['answerId']
    answer_object = answer_get_handler.get_answer_by_id(answer_id)


    try:
        upvote_object = Upvote.objects.filter(user_id=username, answer=answer_object).first()
        if upvote_object:
            upvote_object.delete()


        downvote_object, is_created = Downvote.objects.get_or_create(user_id=username, answer=answer_object)
        return downvote_object

    except Exception as e:
        raise InternalServerError()
    return  None


    # try:
    #     downvote_object, is_created = Downvote.objects.get_or_create(user_id=username, answer=answer_object)
    #     return downvote_object
    #
    # except Exception as e:
    #     print e
    #     return InternalServerError()
