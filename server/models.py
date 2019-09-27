from sql_alchemy_db_instance import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(500))
    done = db.Column(db.Boolean)