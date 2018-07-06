from feed_service.db.feed_models.models import Answer
from feed_service.utils.exceptions import NotFoundException


def get_answer_for_question(question_id):
    answer_object = Answer.objects.filter(question_id=question_id)
    return answer_object
def get_all_answer():
    return Answer.objects.all()


def get_answer_by_id(answer_id):

    #print "Hello"
    # print answer_id
    try:
        answer_object = Answer.objects.get(id=answer_id)
        return answer_object
    except Exception as e:
        print e
        raise NotFoundException(entity='answer')
