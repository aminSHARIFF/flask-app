from app import db, bcrypt
from app.models.base import BaseModel

class User(BaseModel):
    __tablename__ = 'users'

    # basic user info
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    # role is either 'admin' or 'user', defaults to user
    role = db.Column(db.String(20), default='user')

    # hash the password before saving it
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    # check if the given password matches the stored hash
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    # return a clean dict we can send back as JSON
    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role
        }