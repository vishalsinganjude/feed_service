
from flask import request

from feed_service.db.feed_models.models import Question


def create_question(request_data,username):
#    auth_token = request.cookies.get('auth_key')
    question_string = request_data['questionString']

    try:
        question_object = Question.objects.create(user_id=username,
                                                  question_string=question_string)
        return question_object
    except Exception as e:
        print e
        return None
