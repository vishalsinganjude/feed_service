from feed_service.utils import answer_utils


def get_downvote_dict(dowvote_object):
    response_dict = {"answer": answer_utils.get_answer_dict(dowvote_object.answer),
                     "userId": dowvote_object.user_id}

    return response_dict
