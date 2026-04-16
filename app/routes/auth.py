from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models.user import User
from app import db

auth_bp = Blueprint('auth', __name__)

# register a new user
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # make sure all fields are provided
    if not data or not data.get('username') or not data.get('email') or not data.get('password'):
        return jsonify({"status": "error", "message": "please fill in all fields"}), 400

    # check if email is already taken
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"status": "error", "message": "email already in use"}), 400

    # create the user and hash their password
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    user.save()

    return jsonify({"status": "success", "message": "account created", "data": user.to_dict()}), 201


# login and get a token back
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    user = User.query.filter_by(email=data.get('email')).first()

    # wrong email or wrong password
    if not user or not user.check_password(data.get('password', '')):
        return jsonify({"status": "error", "message": "wrong email or password"}), 401

    # generate a JWT token for this user
    token = create_access_token(identity=str(user.id))

    return jsonify({
        "status": "success",
        "data": {
            "token": token,
            "user": user.to_dict()
        }
    }), 200


# get the currently logged in user
@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    return jsonify({"status": "success", "data": user.to_dict()}), 200