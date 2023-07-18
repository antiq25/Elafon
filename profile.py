from application import app, db
from application import Group, Technician, Tool, Key, Signout, ErrorLog

with app.app_context():
    db.create_all()

