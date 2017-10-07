from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from application import db, login_manager


class User(UserMixin, db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(20), index=True, unique=True)
    first_name = db.Column(db.String(15), index=True)
    last_name = db.Column(db.String(15), index=True)
    password_hash = db.Column(db.String(128))
    is_verified = db.Column(db.Boolean, default=False)
    is_admin = db.Column(db.Boolean, default=False)
    creation_datetime = db.Column(db.DateTime, default=datetime.utcnow())
    last_login_datetime = db.Column(db.DateTime, default=datetime.utcnow())
    general_objects = db.relationship('General', backref='user', lazy='dynamic')
    event_objects = db.relationship('Event', backref='user', lazy='dynamic')
    announcement_object = db.relationship('Announcement', backref='user', lazy='dynamic')

    @property
    def password(self):
        """prevent password from being accessed"""
        raise AttributeError('Password is not a readable attribute')

    @password.setter
    def password(self, password):
        """Set password to a hashed password"""
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """Check if hashed password matches the actual password"""
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Employee: {}>'.format(self.username)


@login_manager.user_loader  # set up user_loader // needed by flask login
def load_user(user_id):
    return User.query.get(int(user_id))


class Permission(db.Model):

    __tablename__ = 'permissions'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    general = db.Column(db.Boolean, default=False)
    announcements = db.Column(db.Boolean, default=False)
    events = db.Column(db.Boolean, default=False)

    def __repr__(self):
        permission_list = ['0', '0', '0']
        permission_list[0] = '1' if self.general else '0'
        permission_list[1] = '1' if self.announcements else '0'
        permission_list[2] = '1' if self.events else '0'

        return '<Permission: {}:{}>'.format(self.user_id, ''.join(permission_list))


class Base:
    description = db.Column(db.String(100))
    url = db.Column(db.String(200))
    content = db.Column(db.Text)
    creation_date = db.Column(db.DateTime, default=datetime.utcnow())
    edited_on_date = db.Column(db.DateTime, default=datetime.utcnow())


class Announcement(Base, db.Model):
    __tablename__ = 'announcements'
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    edited_by = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Announcement: {}>'.format(self.description)


class Event(Base, db.Model):

    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    edited_by = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Event: {}>'.format(self.description)


class General(Base, db.Model):

    __tablename__ = 'generals'
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    edited_by = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<General: {}>'.format(self.description)
