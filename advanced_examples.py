"""
Advanced API Examples for When You're Ready!
============================================

These examples show more advanced API concepts for when you've
mastered the basics in api_examples.py

Run this after you understand the basic examples.
"""

import requests
import json
import threading
import time
from datetime import datetime

BASE_URL = "http://localhost:5000"

def print_section(title, emoji="🚀"):
    """Helper function to print section headers"""
    print(f"\n{'='*60}")
    print(f"{emoji} {title}")
    print('='*60)

def example_error_handling():
    """Advanced Example: Proper error handling"""
    print_section("Error Handling Techniques", "⚠️")
    
    # Test 1: Handle 404 error
    print("1. Testing 404 error handling...")
    try:
        response = requests.get(f"{BASE_URL}/api/products/999")
        if response.status_code == 404:
            error_data = response.json()
            print(f"✅ Handled 404 properly: {error_data['error']}")
        else:
            print(f"❌ Unexpected status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
    
    # Test 2: Handle validation errors
    print("\n2. Testing validation error handling...")
    try:
        invalid_product = {"name": "Test"}  # Missing required fields
        response = requests.post(f"{BASE_URL}/api/products", json=invalid_product)
        if response.status_code == 400:
            error_data = response.json()
            print(f"✅ Handled validation error: {error_data['error']}")
        else:
            print(f"❌ Expected 400, got: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")

def example_batch_operations():
    """Advanced Example: Creating multiple items efficiently"""
    print_section("Batch Operations", "📦")
    
    # Create multiple products
    new_products = [
        {
            "name": "Vanilla Bean Sorbet",
            "name_vi": "Sorbet Hạt Vani",
            "description": "Classic vanilla with real vanilla beans",
            "price": 52000,
            "category": "sorbet",
            "ingredients": ["vanilla beans", "sugar", "cream"]
        },
        {
            "name": "Lemon Mint Sorbet", 
            "name_vi": "Sorbet Chanh Bạc Hà",
            "description": "Refreshing lemon with fresh mint",
            "price": 48000,
            "category": "sorbet",
            "ingredients": ["lemon juice", "mint", "sugar"]
        },
        {
            "name": "Chocolate Chip Sorbet",
            "name_vi": "Sorbet Sôcôla",
            "description": "Rich chocolate with dark chocolate chips",
            "price": 58000,
            "category": "sorbet",
            "ingredients": ["cocoa", "chocolate chips", "sugar"]
        }
    ]
    
    print(f"Creating {len(new_products)} products...")
    created_products = []
    
    for i, product in enumerate(new_products, 1):
        try:
            response = requests.post(f"{BASE_URL}/api/products", json=product)
            if response.status_code == 201:
                created = response.json()['product']
                created_products.append(created)
                print(f"✅ {i}. Created: {created['name']}")
            else:
                print(f"❌ {i}. Failed to create: {product['name']}")
        except Exception as e:
            print(f"❌ {i}. Error creating {product['name']}: {e}")
    
    print(f"\n📊 Successfully created {len(created_products)} products!")

def example_data_filtering_and_search():
    """Advanced Example: Advanced filtering and search"""
    print_section("Advanced Data Filtering", "🔍")
    
    # Get all products first
    response = requests.get(f"{BASE_URL}/api/products")
    if response.status_code != 200:
        print("❌ Could not fetch products")
        return
    
    all_products = response.json()['products']
    print(f"Total products available: {len(all_products)}")
    
    # Filter by price range (client-side filtering)
    print("\n1. Products under 50,000đ:")
    affordable_products = [p for p in all_products if p['price'] < 50000]
    for product in affordable_products:
        print(f"  - {product['name']}: {product['price']:,}đ")
    
    # Filter by ingredients (client-side filtering)
    print("\n2. Products with 'sugar' ingredient:")
    sugar_products = [p for p in all_products if 'sugar' in p.get('ingredients', [])]
    for product in sugar_products:
        print(f"  - {product['name']}: {', '.join(product['ingredients'])}")
    
    # Search by name (client-side search)
    search_term = "coconut"
    print(f"\n3. Products containing '{search_term}':")
    matching_products = [p for p in all_products if search_term.lower() in p['name'].lower()]
    for product in matching_products:
        print(f"  - {product['name']}: {product['description']}")

def example_performance_monitoring():
    """Advanced Example: Monitor API performance"""
    print_section("Performance Monitoring", "⏱️")
    
    endpoints_to_test = [
        "/api/products",
        "/api/shop",
        "/api/products/1"
    ]
    
    print("Testing response times for different endpoints:")
    
    for endpoint in endpoints_to_test:
        # Test multiple times and calculate average
        times = []
        for _ in range(5):
            start_time = time.time()
            try:
                response = requests.get(f"{BASE_URL}{endpoint}")
                end_time = time.time()
                if response.status_code == 200:
                    times.append(end_time - start_time)
            except Exception as e:
                print(f"❌ Error testing {endpoint}: {e}")
                continue
        
        if times:
            avg_time = sum(times) / len(times)
            min_time = min(times)
            max_time = max(times)
            print(f"✅ {endpoint}:")
            print(f"   Average: {avg_time*1000:.2f}ms")
            print(f"   Min: {min_time*1000:.2f}ms, Max: {max_time*1000:.2f}ms")

def example_concurrent_requests():
    """Advanced Example: Making concurrent API requests"""
    print_section("Concurrent Requests", "🔄")
    
    def make_request(product_id):
        """Make a single product request"""
        try:
            start_time = time.time()
            response = requests.get(f"{BASE_URL}/api/products/{product_id}")
            end_time = time.time()
            
            if response.status_code == 200:
                product = response.json()
                return {
                    'id': product_id,
                    'name': product['name'],
                    'time': end_time - start_time,
                    'status': 'success'
                }
            else:
                return {
                    'id': product_id,
                    'time': end_time - start_time,
                    'status': 'error',
                    'error': f"HTTP {response.status_code}"
                }
        except Exception as e:
            return {
                'id': product_id,
                'status': 'error',
                'error': str(e)
            }
    
    # Test concurrent requests
    product_ids = [1, 2, 3, 1, 2, 3]  # Test with some duplicates
    results = []
    
    print(f"Making {len(product_ids)} concurrent requests...")
    start_time = time.time()
    
    # Create threads for concurrent requests
    threads = []
    for product_id in product_ids:
        thread = threading.Thread(target=lambda pid=product_id: results.append(make_request(pid)))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    total_time = time.time() - start_time
    
    # Print results
    successful = [r for r in results if r['status'] == 'success']
    failed = [r for r in results if r['status'] == 'error']
    
    print(f"✅ Completed {len(successful)} successful requests")
    print(f"❌ {len(failed)} failed requests")
    print(f"⏱️  Total time: {total_time:.2f}s")
    print(f"📊 Average per request: {total_time/len(product_ids):.2f}s")

def example_data_validation():
    """Advanced Example: Client-side data validation"""
    print_section("Data Validation", "✅")
    
    def validate_product_data(product):
        """Validate product data before sending to API"""
        errors = []
        
        # Required fields
        required_fields = ['name', 'description', 'price', 'category']
        for field in required_fields:
            if field not in product or not product[field]:
                errors.append(f"Missing required field: {field}")
        
        # Data type validation
        if 'price' in product:
            try:
                price = float(product['price'])
                if price <= 0:
                    errors.append("Price must be greater than 0")
                elif price > 1000000:
                    errors.append("Price seems unreasonably high")
            except (ValueError, TypeError):
                errors.append("Price must be a valid number")
        
        # String length validation
        if 'name' in product and len(product['name']) > 100:
            errors.append("Product name too long (max 100 characters)")
        
        if 'description' in product and len(product['description']) > 500:
            errors.append("Description too long (max 500 characters)")
        
        return errors
    
    # Test valid product
    valid_product = {
        "name": "Test Validation Product",
        "description": "This product has valid data",
        "price": 45000,
        "category": "sorbet"
    }
    
    errors = validate_product_data(valid_product)
    if not errors:
        print("✅ Valid product data passed validation")
        # Would send to API here
    else:
        print(f"❌ Validation errors: {errors}")
    
    # Test invalid product
    invalid_product = {
        "name": "",  # Empty name
        "description": "Valid description",
        "price": -100,  # Negative price
        "category": "sorbet"
    }
    
    errors = validate_product_data(invalid_product)
    if errors:
        print(f"✅ Invalid product correctly caught errors:")
        for error in errors:
            print(f"   - {error}")

def example_api_documentation():
    """Advanced Example: Automatically document API endpoints"""
    print_section("API Documentation Discovery", "📚")
    
    # Get API root information
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            api_info = response.json()
            print("🌟 API Information:")
            print(f"   Version: {api_info.get('version', 'Unknown')}")
            print(f"   Status: {api_info.get('status', 'Unknown')}")
            
            if 'endpoints' in api_info:
                print("\n📍 Available Endpoints:")
                for name, path in api_info['endpoints'].items():
                    print(f"   {name}: {path}")
                    
                    # Test each endpoint
                    try:
                        test_response = requests.get(f"{BASE_URL}{path}")
                        status_emoji = "✅" if test_response.status_code == 200 else "❌"
                        print(f"      {status_emoji} Status: {test_response.status_code}")
                    except Exception as e:
                        print(f"      ❌ Error: {e}")
    except Exception as e:
        print(f"❌ Could not get API information: {e}")

def main():
    """Run all advanced examples"""
    print("🚀 Green Sorbetto Advanced API Examples")
    print("These examples demonstrate advanced API usage patterns")
    print("Make sure the API server is running (python app.py)")
    
    # Check if API is available
    try:
        response = requests.get(f"{BASE_URL}/", timeout=5)
        if response.status_code != 200:
            print("❌ API server is not responding correctly")
            return
    except requests.exceptions.RequestException:
        print("❌ Cannot connect to API server. Please start it first with: python app.py")
        return
    
    print("✅ API server is running! Starting advanced examples...")
    
    # Run all advanced examples
    example_api_documentation()
    example_error_handling()
    example_data_validation()
    example_data_filtering_and_search()
    example_performance_monitoring()
    example_batch_operations()
    example_concurrent_requests()
    
    print_section("🎉 Advanced Examples Complete!", "🎉")
    print("You've now seen advanced API usage patterns!")
    print("Try implementing these techniques in your own projects.")

if __name__ == "__main__":
    main()