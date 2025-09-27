"""
API Usage Examples for Beginners
================================

This file shows you how to use the Green Sorbetto API.
Run these examples to learn how APIs work!

Before running these examples:
1. Start the API server: python app.py
2. Install requests library: pip install requests
3. Run this file: python api_examples.py
"""

import requests
import json

# API base URL
BASE_URL = "http://localhost:5000"

def print_section(title):
    """Helper function to print section headers"""
    print(f"\n{'='*50}")
    print(f"🍧 {title}")
    print('='*50)

def example_get_all_products():
    """Example: Get all products"""
    print_section("Example 1: Get All Products")
    
    try:
        response = requests.get(f"{BASE_URL}/api/products")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Success! Found {data['count']} products:")
            for product in data['products']:
                print(f"  - {product['name']} ({product['name_vi']}) - {product['price']:,}đ")
        else:
            print(f"❌ Error: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to API. Make sure the server is running!")

def example_get_single_product():
    """Example: Get a specific product"""
    print_section("Example 2: Get Single Product")
    
    try:
        product_id = 1
        response = requests.get(f"{BASE_URL}/api/products/{product_id}")
        
        if response.status_code == 200:
            product = response.json()
            print(f"✅ Product found:")
            print(f"  Name: {product['name']}")
            print(f"  Vietnamese: {product['name_vi']}")
            print(f"  Price: {product['price']:,}đ")
            print(f"  Description: {product['description']}")
            print(f"  Ingredients: {', '.join(product['ingredients'])}")
        else:
            print(f"❌ Error: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to API. Make sure the server is running!")

def example_create_product():
    """Example: Create a new product"""
    print_section("Example 3: Create New Product")
    
    # New product data
    new_product = {
        "name": "Strawberry Delight",
        "name_vi": "Dâu Tây Ngọt Ngào",
        "description": "Fresh strawberry sorbet with natural sweetness",
        "description_vi": "Sorbet dâu tây tươi với vị ngọt tự nhiên",
        "price": 48000,
        "category": "sorbet",
        "ingredients": ["strawberry", "sugar", "lemon juice", "mint"]
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/products",
            json=new_product,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 201:
            data = response.json()
            print("✅ Product created successfully!")
            print(f"  New product ID: {data['product']['id']}")
            print(f"  Name: {data['product']['name']}")
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.json())
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to API. Make sure the server is running!")

def example_filter_products():
    """Example: Filter products by category"""
    print_section("Example 4: Filter Products")
    
    try:
        response = requests.get(f"{BASE_URL}/api/products?category=sorbet")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Found {data['count']} products in '{data['category']}' category:")
            for product in data['products']:
                print(f"  - {product['name']} - {product['price']:,}đ")
        else:
            print(f"❌ Error: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to API. Make sure the server is running!")

def example_get_shop_info():
    """Example: Get shop information"""
    print_section("Example 5: Get Shop Information")
    
    try:
        response = requests.get(f"{BASE_URL}/api/shop")
        
        if response.status_code == 200:
            shop = response.json()
            print("✅ Shop information:")
            print(f"  Name: {shop['name']}")
            print(f"  Slogan: {shop['slogan']}")
            print(f"  Email: {shop['contact']['email']}")
            print(f"  Phone: {shop['contact']['phone']}")
        else:
            print(f"❌ Error: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to API. Make sure the server is running!")

def example_submit_contact():
    """Example: Submit a contact message"""
    print_section("Example 6: Submit Contact Message")
    
    contact_data = {
        "name": "Nguyễn Văn A",
        "email": "customer@example.com",
        "phone": "0123456789",
        "message": "Hello! I love your coconut sorbet. Do you deliver to District 1?"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/api/contact",
            json=contact_data,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 201:
            data = response.json()
            print("✅ Message sent successfully!")
            print(f"  Response: {data['message']}")
            print(f"  Message ID: {data['id']}")
        else:
            print(f"❌ Error: {response.status_code}")
            print(response.json())
            
    except requests.exceptions.ConnectionError:
        print("❌ Error: Could not connect to API. Make sure the server is running!")

def main():
    """Run all examples"""
    print("🍧 Green Sorbetto API Examples")
    print("Make sure the API server is running (python app.py)")
    
    # Test API availability first
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            print("✅ API server is running!")
        else:
            print("❌ API server returned an error")
            return
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API server. Please start it first with: python app.py")
        return
    
    # Run all examples
    example_get_all_products()
    example_get_single_product()
    example_filter_products()
    example_get_shop_info()
    example_create_product()
    example_submit_contact()
    
    print("\n🎉 All examples completed!")
    print("Now try creating your own API requests!")

if __name__ == "__main__":
    main()