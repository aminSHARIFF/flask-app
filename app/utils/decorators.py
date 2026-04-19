from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from app.models.user import User

# use this decorator on any route you want to restrict by role
def role_required(role):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            # first check if there is a valid token
            verify_jwt_in_request()

            # then get the user from the token
            user_id = get_jwt_identity()
            user = User.query.get(user_id)

            # if their role doesnt match, block them
            if not user or user.role != role:
                return jsonify({"status": "error", "message": "you dont have permission"}), 403

            return fn(*args, **kwargs)
        return wrapper
    return decorator