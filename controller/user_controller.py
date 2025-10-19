from flask import Blueprint, jsonify, request
from middleware.auth_middleware import jwt_required
from services.user_service import UserService

user_bp = Blueprint('user_bp', __name__, url_prefix="/api/users")

@user_bp.route('/register', methods=['POST'])
def create_user():
    data = request.get_json()
    result = UserService.create_user(data)
    status_code = 200 if result['sucess'] else 400
    return jsonify(result), status_code

@user_bp.route('/', methods=['GET'])
@jwt_required
def get_users(user_data):
    #list the users
    result = UserService.get_all_users()
    return jsonify(result), 200

@user_bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    result, status_code = UserService.login_user(data)
    return jsonify(result), status_code




