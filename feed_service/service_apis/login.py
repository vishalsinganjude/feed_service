from flask import request, session, make_response, jsonify
from flask_restful import Resource
import json
from feed_service.services import user_service


class Login(Resource):
    def post(self):
        request_data = request.get_json(force=True)
        user_dict = user_service.login(request_data['username'],
                                        request_data['password'],
                                       request_data['clientId'])
        # print user_dict

        if not user_dict:
            return ({},401)

        # print user_dict;
        session['key'] = user_dict['authToken']
        user_dict = user_dict['user']
        session['username'] = user_dict['username']
        session['phone'] = user_dict['phone']
        session['lastName'] = user_dict['lastName']
        session['email'] = user_dict['email']

        response = make_response(json.dumps(user_dict))
        response.set_cookie("auth_key", session['key'])
        response.mimetype = "application/json"
        
        response.headers['Access-Control-Allow-Origin'] = '*'
        # print "Session=======>>>>", session
        return  response