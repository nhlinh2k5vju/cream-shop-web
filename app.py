"""
Green Sorbetto API - A Beginner-Friendly Python API
===================================================

This is a simple Flask API for the Green Sorbetto ice cream shop.
Perfect for beginners learning API development with Python!

What this API does:
- Manages ice cream/sorbet products
- Handles shop information 
- Processes contact form submissions
- Provides data for the frontend website

Author: Beginner API Developer
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime
import os

# Create Flask app
app = Flask(__name__)

# Enable CORS to allow frontend to call our API
CORS(app)

# Sample data - In a real app, this would come from a database
PRODUCTS = [
    {
        "id": 1,
        "name": "Coconut Sorbetto",
        "name_vi": "Sorbetto Dừa",
        "description": "Refreshing coconut sorbet made with fresh coconut milk",
        "description_vi": "Sorbet dừa tươi mát làm từ nước cốt dừa tươi",
        "price": 45000,
        "category": "sorbet",
        "image": "/image/menu-1.png",
        "available": True,
        "ingredients": ["coconut milk", "sugar", "lime juice"]
    },
    {
        "id": 2,
        "name": "Tequila Sunrise",
        "name_vi": "Tequila Sunrise",
        "description": "Orange and strawberry sorbet with a hint of citrus",
        "description_vi": "Sorbet cam và dâu tây với hương vị cam quýt nhẹ",
        "price": 55000,
        "category": "sorbet",
        "image": "/image/menu-2.png",
        "available": True,
        "ingredients": ["orange juice", "strawberry", "sugar", "citrus"]
    },
    {
        "id": 3,
        "name": "Mango Passion",
        "name_vi": "Xoài Chanh Dây",
        "description": "Tropical mango sorbet with passion fruit",
        "description_vi": "Sorbet xoài nhiệt đới với chanh dây",
        "price": 50000,
        "category": "sorbet",
        "image": "/image/menu-3.png",
        "available": True,
        "ingredients": ["mango", "passion fruit", "sugar", "lime"]
    }
]

SHOP_INFO = {
    "name": "Green Sorbetto",
    "slogan": "Sorbet trên tay, nắng bay ngay!",
    "description": "Nơi mỗi món ăn là một tác phẩm nghệ thuật",
    "contact": {
        "email": "contact@greensorbetto.com",
        "phone": "+84375489781",
        "address": "Vietnam"
    },
    "social": {
        "facebook": "https://www.facebook.com/share/19bk6sSwVn/?mibextid=wwXIfr",
        "instagram": "https://www.instagram.com/greensorbetto.vn?igsh=cnhvZm04YnJ3ejB4",
        "tiktok": "https://www.tiktok.com/@greensorbetto.vn?_t=ZS-8yJiZrBprbG&_r=1"
    }
}

# Store contact messages (in real app, save to database)
CONTACT_MESSAGES = []

# ============================================================================
# API ENDPOINTS - Learn how to build REST APIs!
# ============================================================================

@app.route('/')
def home():
    """
    Home endpoint - Returns basic API information
    This is often called the 'root' or 'health check' endpoint
    """
    return jsonify({
        "message": "Welcome to Green Sorbetto API!",
        "message_vi": "Chào mừng đến với API Green Sorbetto!",
        "version": "1.0.0",
        "status": "running",
        "endpoints": {
            "products": "/api/products",
            "shop_info": "/api/shop",
            "contact": "/api/contact"
        }
    })

@app.route('/api/products', methods=['GET'])
def get_products():
    """
    GET /api/products - Get all products
    
    This endpoint returns all available products.
    You can filter by category using ?category=sorbet
    """
    # Get category filter from URL parameter
    category = request.args.get('category')
    
    # Filter products if category is specified
    if category:
        filtered_products = [p for p in PRODUCTS if p['category'] == category]
        return jsonify({
            "products": filtered_products,
            "count": len(filtered_products),
            "category": category
        })
    
    # Return all products
    return jsonify({
        "products": PRODUCTS,
        "count": len(PRODUCTS)
    })

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    GET /api/products/{id} - Get a specific product
    
    This endpoint returns details for a single product.
    Example: GET /api/products/1
    """
    # Find product by ID
    product = next((p for p in PRODUCTS if p['id'] == product_id), None)
    
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    return jsonify(product)

@app.route('/api/products', methods=['POST'])
def create_product():
    """
    POST /api/products - Create a new product
    
    This endpoint allows you to add new products.
    Requires JSON data in the request body.
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'description', 'price', 'category']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        # Create new product
        new_product = {
            "id": len(PRODUCTS) + 1,  # Simple ID generation
            "name": data['name'],
            "name_vi": data.get('name_vi', data['name']),
            "description": data['description'],
            "description_vi": data.get('description_vi', data['description']),
            "price": data['price'],
            "category": data['category'],
            "image": data.get('image', '/image/default.png'),
            "available": data.get('available', True),
            "ingredients": data.get('ingredients', [])
        }
        
        # Add to products list
        PRODUCTS.append(new_product)
        
        return jsonify({
            "message": "Product created successfully!",
            "product": new_product
        }), 201
        
    except Exception as e:
        return jsonify({"error": "Invalid data format"}), 400

@app.route('/api/shop', methods=['GET'])
def get_shop_info():
    """
    GET /api/shop - Get shop information
    
    Returns general information about the shop.
    """
    return jsonify(SHOP_INFO)

@app.route('/api/contact', methods=['POST'])
def submit_contact():
    """
    POST /api/contact - Submit a contact message
    
    Allows customers to send messages to the shop.
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'email', 'message']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        # Create contact message
        contact_message = {
            "id": len(CONTACT_MESSAGES) + 1,
            "name": data['name'],
            "email": data['email'],
            "phone": data.get('phone', ''),
            "message": data['message'],
            "timestamp": datetime.now().isoformat(),
            "status": "new"
        }
        
        # Store message
        CONTACT_MESSAGES.append(contact_message)
        
        return jsonify({
            "message": "Thank you for your message! We'll get back to you soon.",
            "message_vi": "Cảm ơn bạn đã liên hệ! Chúng tôi sẽ phản hồi sớm nhất có thể.",
            "id": contact_message['id']
        }), 201
        
    except Exception as e:
        return jsonify({"error": "Invalid data format"}), 400

@app.route('/api/contact', methods=['GET'])
def get_contact_messages():
    """
    GET /api/contact - Get all contact messages (for admin)
    
    Returns all contact messages. In a real app, this would require authentication.
    """
    return jsonify({
        "messages": CONTACT_MESSAGES,
        "count": len(CONTACT_MESSAGES)
    })

# ============================================================================
# ERROR HANDLERS - Handle errors gracefully
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({"error": "Internal server error"}), 500

# ============================================================================
# RUN THE APP
# ============================================================================

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    
    # Run the app
    print("🍧 Starting Green Sorbetto API...")
    print(f"🌐 API will be available at: http://localhost:{port}")
    print("📖 Visit http://localhost:5000 for API information")
    
    # Debug mode is great for learning - shows detailed errors
    app.run(host='0.0.0.0', port=port, debug=True)