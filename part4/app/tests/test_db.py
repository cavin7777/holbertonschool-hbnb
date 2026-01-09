from app import create_app, db

app = create_app()

with app.app_context():
#    db.drop_all()      # drops all tables
    db.create_all()

# (.venv) PS C:\Users\dell\Desktop\Holberton_HBNB\holbertonschool-hbnb\part3> python -m app.tests.test_db  