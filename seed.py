from app import create_app, db
from app.models.products import Product
from app.models.user import User

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
    
    admin = User(username="admin", email="admin@test.com", role="admin")
    admin.set_password("password")

    user = User(username="user", email="user@test.com", role="user")
    user.set_password("password")

    db.session.add_all([admin, user])

    p1 = Product(name="Laptop", price=50000, stock=10)
    p2 = Product(name="Phone", price=20000, stock=15)
    p3 = Product(name="Keyboard", price=3000, stock=25)

    db.session.add_all([p1, p2, p3])

    db.session.commit()

    print("🌱 Database seeded successfully!")