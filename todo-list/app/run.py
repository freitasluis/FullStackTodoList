from initApp import create_app # Import the factory function
from dbModels import db # Import the database

# Create the Flask app using the factory function
app = create_app()

if __name__ == "__main__":
    # Ensure tables are created within the app context
    with app.app_context():
        db.create_all()

    # Start the Flask application
    app.run(debug=True)