from functools import wraps
from flask import request, jsonify
from security.jwt_util import JwtUtil

def jwt_required(f): #middleware decorator for all routes!
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return jsonify({"success": False, "message": "Missing token",})
        
        try:
            token = auth_header.split(" ")[1]
        except IndexError:
            return jsonify({"success": False, "message": "token format invalid",})

        verification = JwtUtil.verify_token(token)

        if not verification["valid"]:
            return jsonify({"success": False, "message": verification["message"]}), 401

        user_data = verification["data"]
        #request.user = verification["data"]
        kwargs['user_data'] = user_data

        return f(*args, **kwargs)
    return decorated   