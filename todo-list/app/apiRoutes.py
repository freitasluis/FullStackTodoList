from flask import request, jsonify
from flask_restful import Api, Resource
from dbModels import db, Todo

api = Api()

class TodoResource(Resource):
    def get(self):
        """
                Handles GET requests to retrieve all To-Do items.
                Queries the database for all To do items and returns them as a JSON response.
        """
        todotasks = Todo.query.all() # Retrieve all to-dos from the database
        return jsonify([{"id": t.id, "title": t.title, "completed": t.completed} for t in todotasks]) # Convert to JSON

    def post(self):
        """
                Handles POST requests to add a new To-Do item.
                Reads the incoming JSON data, creates a new To do item, saves it to the database,
                and returns a success message.
        """
        data = request.json # Extract JSON data from the request body
        new_todo_task = Todo(title=data["title"]) # Create a new To-do object
        db.session.add(new_todo_task) # Add the new object to the database session
        db.session.commit() # Commit the session to save changes to the database
        return jsonify({"message": "To Do Task added!"})

# Register the TodoResource with the API, so it handles requests to "/todos"
api.add_resource(TodoResource, "/todos")