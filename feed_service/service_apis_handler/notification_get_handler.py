from feed_service.db.feed_models.models import Notification


def get_Notification_By_UserId(user_object):
    Notification_object = Notification.objects.filter(owner_id=user_object['username'], is_read=False)
    return Notification_object

