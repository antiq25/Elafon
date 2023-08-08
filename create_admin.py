from app import db, Technician
from werkzeug.security import generate_password_hash

def create_admin():
    with app.app_context():
        # Check if an admin account already exists
        if not Technician.query.filter_by(role='admin').first():
            # Create a new admin account
            admin = Technician(name='admin', role='admin')
            admin.password = generate_password_hash('admin')
            db.session.add(admin)
            db.session.commit()
            print("Admin account created.")
        else:
            print("Admin account already exists.")

if __name__ == "__main__":
    create_admin()

