from flask import request, jsonify
from functools import wraps
import secrets
import decimal
import requests
import json

from sqlalchemy import DECIMAL

from fitness_tracker.models import User


def token_required(our_flask_function):
    @wraps(our_flask_function)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'].split()[1]
            print(token)

            if not token:
                return jsonify({'message': 'Token is missing'}), 401 #Client error
            
            try:
                our_user =User.query.filter_by(token=token).first()
                print(our_user)
                if not our_user or our_user.token !=token:
                    return jsonify({'message': 'Token is Invalid'}), 401 #Client error
                
            except:
                our_user = User.query.filter_by(token=token).first()
                if token != our_user.token and secrets.compare_digest(token, our_user.token):
                    return jsonify({'message': 'Token is Invalid'}), 401
            return our_flask_function(our_user, *args, **kwargs)
        return decorated 
    

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal,DECIMAL):
            return str(obj)
        return json.JSONEncoder(JSONEncoder, self).default(obj)
