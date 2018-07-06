def get_question_dict(question_object):
    question_dict = {
                    "id": question_object.id,
                    "userId": question_object.user_id,
                     "questionString": question_object.question_string,
                     "createdDate": question_object.created_date.strftime(
                         "%d/%m/%y")}
    return question_dict
