from app import db
from app.models.base import BaseModel

class Product(BaseModel):
    __tablename__ = "products"
    
    name = db.Column(db.String, nullable = False)
    price = db.Column(db.Float, nullable = False)
    stock = db.Column(db.Integer, nullable = False)
    
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    supplier_id = db.Column(db.Integer, db.ForeignKey("suppliers.id"))
    
    transactions = db.relationship("InventoryTransaction", back_populates="product")