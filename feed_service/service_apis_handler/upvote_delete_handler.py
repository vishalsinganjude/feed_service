from feed_service.db.feed_models.models import Upvote
from feed_service.utils.exceptions import NotFoundException


def delete_upvote(request_data):
    user_id = request_data['userId']
    answer_id = request_data['answerId']

    try:
        upvote_object = Upvote.objects.get(user_id=user_id,answer_id=answer_id)
        temp_object = upvote_object
        upvote_object.delete()
        return temp_object

    except Exception as e:
        print e
        raise NotFoundException(entity="upvote")