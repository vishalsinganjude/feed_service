from feed_service.db.feed_models.models import Question, Answer

notification_to_string_map = {
    'Answer':" has answered your question ",
    'Upvote':"has Upvoted your Answer",
    'Downvote':"has Downvoted your Answer"
}

def get_Notification_by_response_dict(notification_objects):
    response_dict = []
    for entry in notification_objects:
        if entry.entity_type == "Answer":
            question_object = Question.objects.get(id=entry.entity_id)
            response = {
                'notificationString': entry.action_by + " "+notification_to_string_map[
                    entry.entity_type] + " '"+question_object.question_string+"'",
                'id': entry.id
            }

        elif entry.entity_type in ["Upvote", "Downvote"] :
            answer_object = Answer.objects.get(id=entry.entity_id)
            response = {
                'notificationString': entry.action_by + " "+notification_to_string_map[
                    entry.entity_type] + " '"+answer_object.answer_string+"'",
                'id':entry.id
            }

        response_dict.append(response)

    return response_dict



