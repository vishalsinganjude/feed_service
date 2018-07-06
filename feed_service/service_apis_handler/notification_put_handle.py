from feed_service.db.feed_models.models import Notification


def read_all_notification(Notification_object):

    for x in Notification_object:
        x.is_read = True;
        x.save();
        print "Notification Status---->", x.is_read;

    return None
