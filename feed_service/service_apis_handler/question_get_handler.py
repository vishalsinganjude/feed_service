from feed_service.db.feed_models.models import Question
from feed_service.utils.exceptions import NotFoundException


def get_question_for_user(user_id):
    question_objects = Question.objects.filter(user_id=user_id)
    return question_objects


def get_all_questions():
    return Question.objects.all()


def get_question_by_id(question_id):
    try:
        question_object = Question.objects.get(id=question_id)
        return question_object
    except Exception as e:
        raise NotFoundException(entity='Question')
