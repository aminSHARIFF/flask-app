from app import db
from app.models.base import BaseModel

class InventoryTransaction(BaseModel):
    __tablename__ = "inventory_transactions"
    
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String, nullable=False)
    # Type should indicate IN or OUT stock movement