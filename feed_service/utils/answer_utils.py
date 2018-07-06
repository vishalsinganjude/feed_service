from feed_service.utils import question_utils


def get_answer_dict(answer_object):
    response_dict = {"answerId": answer_object.id,
                    "question" : question_utils.get_question_dict(answer_object.question),
                     "userId" : answer_object.user_id,
                     "answerString" : answer_object.answer_string,
                     "createdDate": answer_object.created_date.strftime("%d/%m/%y")}
    return response_dict