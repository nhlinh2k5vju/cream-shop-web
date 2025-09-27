"""
Simple API Tests for Beginners
==============================

This file contains basic tests to make sure your API works correctly.
Great for learning how to test APIs!

To run tests: python test_api.py
"""

import requests
import json

def test_api_connection():
    """Test if API server is running"""
    print("🔍 Testing API connection...")
    try:
        response = requests.get("http://localhost:5000/")
        if response.status_code == 200:
            print("✅ API server is running!")
            return True
        else:
            print(f"❌ API returned status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to API. Make sure server is running!")
        return False

def test_get_products():
    """Test getting all products"""
    print("\n🔍 Testing GET /api/products...")
    try:
        response = requests.get("http://localhost:5000/api/products")
        if response.status_code == 200:
            data = response.json()
            if 'products' in data and len(data['products']) > 0:
                print(f"✅ Successfully got {data['count']} products")
                return True
            else:
                print("❌ No products found in response")
                return False
        else:
            print(f"❌ Request failed with status {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def test_get_single_product():
    """Test getting a single product"""
    print("\n🔍 Testing GET /api/products/1...")
    try:
        response = requests.get("http://localhost:5000/api/products/1")
        if response.status_code == 200:
            product = response.json()
            if 'name' in product and 'price' in product:
                print(f"✅ Successfully got product: {product['name']}")
                return True
            else:
                print("❌ Product missing required fields")
                return False
        else:
            print(f"❌ Request failed with status {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def test_get_shop_info():
    """Test getting shop information"""
    print("\n🔍 Testing GET /api/shop...")
    try:
        response = requests.get("http://localhost:5000/api/shop")
        if response.status_code == 200:
            shop = response.json()
            if 'name' in shop and 'contact' in shop:
                print(f"✅ Successfully got shop info: {shop['name']}")
                return True
            else:
                print("❌ Shop info missing required fields")
                return False
        else:
            print(f"❌ Request failed with status {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def test_create_product():
    """Test creating a new product"""
    print("\n🔍 Testing POST /api/products...")
    
    test_product = {
        "name": "Test Sorbet",
        "description": "A test product for API validation",
        "price": 40000,
        "category": "sorbet"
    }
    
    try:
        response = requests.post(
            "http://localhost:5000/api/products",
            json=test_product,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 201:
            data = response.json()
            if 'product' in data and data['product']['name'] == test_product['name']:
                print(f"✅ Successfully created product: {data['product']['name']}")
                return True
            else:
                print("❌ Created product doesn't match expected data")
                return False
        else:
            print(f"❌ Request failed with status {response.status_code}")
            print(response.text)
            return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def test_contact_submission():
    """Test submitting a contact message"""
    print("\n🔍 Testing POST /api/contact...")
    
    test_message = {
        "name": "Test User",
        "email": "test@example.com",
        "message": "This is a test message for API validation"
    }
    
    try:
        response = requests.post(
            "http://localhost:5000/api/contact",
            json=test_message,
            headers={'Content-Type': 'application/json'}
        )
        
        if response.status_code == 201:
            data = response.json()
            if 'message' in data and 'id' in data:
                print(f"✅ Successfully submitted contact message (ID: {data['id']})")
                return True
            else:
                print("❌ Contact response missing required fields")
                return False
        else:
            print(f"❌ Request failed with status {response.status_code}")
            print(response.text)
            return False
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

def run_all_tests():
    """Run all API tests"""
    print("🧪 Green Sorbetto API Tests")
    print("="*40)
    
    tests = [
        test_api_connection,
        test_get_products,
        test_get_single_product,
        test_get_shop_info,
        test_create_product,
        test_contact_submission
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "="*40)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your API is working perfectly!")
    else:
        print("⚠️  Some tests failed. Check the errors above.")
        print("💡 Make sure the API server is running: python app.py")
    
    return passed == total

if __name__ == "__main__":
    run_all_tests()