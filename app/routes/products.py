from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app import db
from app.models.products import Product

products_bp = Blueprint('products_bp', __name__)

#

@products_bp.route('/', methods=['POST'])
@jwt_required()
def create_product():
    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "No input data provided"
        }), 400

    name = data.get('name')
    price = data.get('price')
    stock = data.get('stock', 0)

    if not name:
        return jsonify({
            "status": "error",
            "message": "Product name is required"
        }), 400

    if price is None or price < 0:
        return jsonify({
            "status": "error",
            "message": "Valid price is required"
        }), 400

    product = Product(
        name=name,
        price=price,
        stock=stock
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Product created successfully",
        "data": {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock
        }
    }), 201

@products_bp.route('/', methods=['GET'])
def get_products():
    products = Product.query.all()

    return jsonify({
        "status": "success",
        "data": [
            {
                "id": p.id,
                "name": p.name,
                "price": p.price,
                "stock": p.stock
            } for p in products
        ]
    }), 200

@products_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get(product_id)

    if not product:
        return jsonify({
            "status": "error",
            "message": "Product not found"
        }), 404

    return jsonify({
        "status": "success",
        "data": {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock
        }
    }), 200

@products_bp.route('/<int:product_id>', methods=['PATCH'])
@jwt_required()
def update_product(product_id):
    product = Product.query.get(product_id)

    if not product:
        return jsonify({
            "status": "error",
            "message": "Product not found"
        }), 404

    data = request.get_json()

    if 'name' in data:
        product.name = data['name']

    if 'price' in data:
        if data['price'] < 0:
            return jsonify({
                "status": "error",
                "message": "Price cannot be negative"
            }), 400
        product.price = data['price']

    if 'stock' in data:
        if data['stock'] < 0:
            return jsonify({
                "status": "error",
                "message": "Stock cannot be negative"
            }), 400
        product.stock = data['stock']

    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Product updated successfully",
        "data": {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "stock": product.stock
        }
    }), 200

@products_bp.route('/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product(product_id):
    product = Product.query.get(product_id)

    if not product:
        return jsonify({
            "status": "error",
            "message": "Product not found"
        }), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Product deleted successfully"
    }), 200