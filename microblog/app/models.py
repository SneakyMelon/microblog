"""
Models and Database management.
"""


from app import db


class User(db.Model):
    """
    Create a new user for storing in the database.

    ```Example Queries```::

        users = models.User.query.all() # Get all users
        users = models.User.query.get(id_of_user)
        users = models.User.query.order_by('nickname desc').all()
    """
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.nickname


class Post(db.Model):
    """
    Creates a new Post, created by a User.

    :Relationship: Post *..1 User
    """
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
