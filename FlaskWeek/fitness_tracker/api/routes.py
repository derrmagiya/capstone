from flask import Blueprint, request, jsonify
from fitness_tracker.helpers import token_required
from fitness_tracker.models import db, Fitness, fitness_schema, fitnesses_schema

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'some': 'value'}

