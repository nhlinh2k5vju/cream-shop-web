# 🛠️ Development Guide

## Quick Start Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Start the API server
python app.py
# OR use the easy starter
python run_server.py

# Test the API
python test_api.py

# Try basic examples
python api_examples.py

# Try advanced examples (when ready)
python advanced_examples.py
```

## File Structure Explained

```
📁 cream-shop-web/
├── 🌐 Frontend Files
│   ├── index.html          # Main website
│   ├── about.html          # About page
│   ├── style.css           # Website styles
│   ├── script.js           # Website JavaScript
│   ├── api-demo.html       # API demo page
│   └── image/              # Website images
│
├── 🐍 Backend API Files
│   ├── app.py              # Main API server
│   ├── run_server.py       # Easy server starter
│   ├── requirements.txt    # Python dependencies
│   └── .gitignore          # Git ignore file
│
├── 📚 Learning Files
│   ├── api_examples.py     # Basic API examples
│   ├── advanced_examples.py # Advanced examples
│   ├── test_api.py         # API tests
│   ├── README.md           # Main documentation
│   └── DEVELOPMENT.md      # This file
│
└── 🔧 Config Files
    └── .gitignore          # Files to ignore in Git
```

## API Endpoints Reference

### 🏠 Root Endpoint
- `GET /` - API information and health check

### 🍨 Products
- `GET /api/products` - Get all products
- `GET /api/products?category=sorbet` - Filter by category
- `GET /api/products/{id}` - Get specific product
- `POST /api/products` - Create new product

### 🏪 Shop
- `GET /api/shop` - Get shop information

### 📧 Contact
- `POST /api/contact` - Submit contact message
- `GET /api/contact` - Get all messages (admin)

## Adding New Features

### Adding a New Endpoint

1. **Define the route in `app.py`:**
```python
@app.route('/api/your-endpoint', methods=['GET'])
def your_function():
    # Your code here
    return jsonify({"message": "Hello World!"})
```

2. **Test it:**
```bash
curl http://localhost:5000/api/your-endpoint
```

3. **Add to examples:**
Add a test function in `test_api.py` and `api_examples.py`

### Adding New Data Fields

1. **Update the sample data in `app.py`:**
```python
PRODUCTS = [
    {
        "id": 1,
        "name": "Product",
        "your_new_field": "your_value",  # Add this
        # ... other fields
    }
]
```

2. **Update validation if needed:**
```python
required_fields = ['name', 'description', 'price', 'category', 'your_new_field']
```

## Common Beginner Mistakes

### ❌ Server Not Running
**Error:** `Connection refused` or `Cannot connect`
**Solution:** Make sure to run `python app.py` first

### ❌ Wrong Port
**Error:** API calls failing
**Solution:** Check if server is running on port 5000 (default)

### ❌ Missing Headers
**Error:** `400 Bad Request` when sending JSON
**Solution:** Add proper headers:
```python
headers = {'Content-Type': 'application/json'}
requests.post(url, json=data, headers=headers)
```

### ❌ Forgetting JSON
**Error:** Server gets empty data
**Solution:** Use `json=data` not `data=data` in requests

## Testing Your API

### Manual Testing
```bash
# Test GET endpoint
curl http://localhost:5000/api/products

# Test POST endpoint
curl -X POST http://localhost:5000/api/products \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","price":1000,"category":"test","description":"Test"}'
```

### Python Testing
```python
import requests

# GET request
response = requests.get('http://localhost:5000/api/products')
print(response.json())

# POST request
data = {"name": "Test Product", "price": 5000}
response = requests.post('http://localhost:5000/api/products', json=data)
print(response.json())
```

### Browser Testing
1. Start the server: `python app.py`
2. Open `api-demo.html` in your browser
3. Click buttons to test different endpoints

## Debugging Tips

### Check Server Logs
Look at the terminal where you ran `python app.py` - it shows all requests and errors.

### Use Debug Mode
Debug mode is enabled by default. It shows detailed error messages.

### Print Debugging
Add print statements to your code:
```python
@app.route('/api/test')
def test_endpoint():
    print("This endpoint was called!")  # Debug info
    return jsonify({"status": "ok"})
```

### Browser Developer Tools
1. Press F12 in browser
2. Go to Network tab
3. Make API calls
4. See request/response details

## Next Steps for Learning

### Beginner → Intermediate
1. ✅ Master basic CRUD operations
2. ✅ Learn HTTP status codes
3. ✅ Understand JSON data format
4. 🔄 Add input validation
5. 🔄 Learn about databases (SQLite)
6. 🔄 Add user authentication

### Intermediate → Advanced
1. 🔄 Use a real database (PostgreSQL)
2. 🔄 Add authentication & authorization
3. 🔄 Implement file uploads
4. 🔄 Add API rate limiting
5. 🔄 Deploy to production (Heroku, AWS)
6. 🔄 Add API documentation (Swagger)

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [HTTP Status Codes](https://httpstatuses.com/)
- [JSON Format Guide](https://www.json.org/)
- [REST API Best Practices](https://restfulapi.net/)

## Need Help?

1. **Read the error messages** - they often tell you exactly what's wrong
2. **Check the server logs** - look at the terminal where you ran the server
3. **Use the examples** - `api_examples.py` shows working code
4. **Test incrementally** - test each small change before moving on
5. **Use debugging tools** - print statements, browser dev tools, etc.

Happy coding! 🍧✨