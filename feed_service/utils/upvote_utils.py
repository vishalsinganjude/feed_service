from feed_service.utils import answer_utils


def get_upvote_dict(upvote_object):
    response_dict = {"id": upvote_object.id,
                     "userId":upvote_object.user_id,
                     "answer":answer_utils.get_answer_dict(upvote_object.answer)
                     }
    return response_dict