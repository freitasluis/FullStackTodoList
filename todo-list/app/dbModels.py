from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # Creates a database instance

# Defines the To-Do model (OOP)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Todo {self.title}>"