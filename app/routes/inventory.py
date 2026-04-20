from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models.products import Product
from app.models.inventory import InventoryTransaction
from app.utils.decorators import role_required


inventory_bp = Blueprint('inventory_bp', __name__)



@inventory_bp.route('/in/<int:product_id>', methods=['POST'])
@jwt_required()
@role_required('admin')
def stock_in(product_id):
    product = Product.query.get(product_id)

    if not product:
        return jsonify({
            "status": "error",
            "message": "Product not found"
        }), 404

    data = request.get_json()
    quantity = data.get('quantity')

    if quantity is None or quantity <= 0:
        return jsonify({
            "status": "error",
            "message": "Quantity must be greater than 0"
        }), 400

    product.stock += quantity
    
    transaction = InventoryTransaction(
        product_id=product.id,
        quantity=quantity,
        type="IN"
    )
    db.session.add(transaction)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": f"Added {quantity} units to stock",
        "data": {
            "product_id": product.id,
            "name": product.name,
            "new_stock": product.stock
        }
    }), 200

@inventory_bp.route('/out/<int:product_id>', methods=['POST'])
@jwt_required()
@role_required('admin')
def stock_out(product_id):
    product = Product.query.get(product_id)

    if not product:
        return jsonify({
            "status": "error",
            "message": "Product not found"
        }), 404

    data = request.get_json()
    quantity = data.get('quantity')

    if quantity is None or quantity <= 0:
        return jsonify({
            "status": "error",
            "message": "Quantity must be greater than 0"
        }), 400

    if product.stock < quantity:
        return jsonify({
            "status": "error",
            "message": "Insufficient stock"
        }), 400

    product.stock -= quantity
    
    transaction = InventoryTransaction(
        product_id=product.id,
        quantity=quantity,
        type="OUT"
    )

    db.session.add(transaction)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": f"Removed {quantity} units from stock",
        "data": {
            "product_id": product.id,
            "name": product.name,
            "new_stock": product.stock
        }
    }), 200

@inventory_bp.route('/', methods=['GET'])
def get_inventory():
    products = Product.query.all()

    return jsonify({
        "status": "success",
        "data": [
            {
                "product_id": p.id,
                "name": p.name,
                "stock": p.stock
            } for p in products
        ]
    }), 200

@inventory_bp.route('/transactions/<int:product_id>', methods=['GET'])
@jwt_required()
def get_transactions(product_id):
    transactions = InventoryTransaction.query.filter_by(product_id=product_id).all()

    return jsonify({
        "status": "success",
        "data": [
            {
                "id": t.id,
                "quantity": t.quantity,
                "type": t.type
            } for t in transactions
        ]
    }), 200