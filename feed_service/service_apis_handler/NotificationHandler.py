from feed_service.db.feed_models.models import Notification


def create_Notification_Object(entity_type, entity_id, action_by, owner_by):

    try:
        notification_object = Notification.objects.get_or_create(entity_type=entity_type, entity_id=entity_id, action_by=action_by, owner_id=owner_by)
        return notification_object

    except Exception as e:
        print e
        return None




