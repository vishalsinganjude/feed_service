import django
django.setup()
from feed_service.service_apis.Notification import Notification


from flask import Flask
from flask_restful import Api


from feed_service.service_apis.feeds import Feed
from feed_service.service_apis.login import Login
from feed_service.service_apis.downvote import Downvote
from feed_service.service_apis.upvote import Upvote
from feed_service.service_apis.answer import Answer
from feed_service.service_apis.ping import Ping
from feed_service.service_apis.question import Question

app = Flask(__name__)
api = Api(app, prefix='/feedservice/')
app.secret_key = 'super secret key'

api.add_resource(Ping, 'ping/')
api.add_resource(Question, 'question/', 'question/<string:user_id>/')
api.add_resource(Answer, 'answer/', 'answer/<string:answer_id>/')
api.add_resource(Upvote, 'upvote/')
api.add_resource(Downvote, 'downvote/')
api.add_resource(Login, 'login/')
api.add_resource(Feed, 'feed/')
api.add_resource(Notification, 'notification/')


if __name__ == "__main__":
    app.run(host='localhost', port=8091, debug=True)

