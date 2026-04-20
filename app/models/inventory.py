from app import db
from app.models.base import BaseModel

class InventoryTransaction(BaseModel):
    __tablename__ = "Inventory_transactions"
    
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable = False)
    quantity = db.Column(db.Integer, nullable = False)
    type = db.Column(db.String, nullable = False)
    # Type should dictate whether a transaction is 
    # incoming or outgoing like if product is coming 
    # in vs being sold please correct if im wrong on that