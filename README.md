# 🍧 Green Sorbetto - Cream Shop Web & API

A beginner-friendly project combining a beautiful ice cream shop website with a Python API. Perfect for learning web development and API creation!

## 🌟 What This Project Contains

### Frontend (Website)
- **Beautiful Vietnamese ice cream shop website**
- Modern HTML5, CSS3, and JavaScript
- Responsive design with Tailwind CSS
- Interactive animations and smooth scrolling

### Backend (API)
- **Python Flask API for beginners**
- RESTful endpoints for products, shop info, and contact
- Well-documented code with comments
- Example usage scripts included

## 🚀 Getting Started with the API

### Prerequisites
- Python 3.7 or higher
- Basic knowledge of Python (variables, functions, dictionaries)

### Quick Start

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the API server:**
   ```bash
   python run_server.py
   ```

3. **Visit the API in your browser:**
   - Open http://localhost:5000 for API information
   - View the website by opening `index.html` in your browser

4. **Try the API examples:**
   ```bash
   python api_examples.py
   ```

## 📖 API Documentation

### Base URL
```
http://localhost:5000
```

### Available Endpoints

#### 🏠 Home
- **GET** `/` - API information and health check

#### 🍨 Products
- **GET** `/api/products` - Get all products
- **GET** `/api/products?category=sorbet` - Filter by category
- **GET** `/api/products/{id}` - Get specific product
- **POST** `/api/products` - Create new product

#### 🏪 Shop Information
- **GET** `/api/shop` - Get shop details and contact info

#### 📧 Contact
- **POST** `/api/contact` - Submit contact message
- **GET** `/api/contact` - Get all messages (admin)

### Example API Calls

#### Get All Products
```bash
curl http://localhost:5000/api/products
```

#### Create New Product
```bash
curl -X POST http://localhost:5000/api/products \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Chocolate Sorbet",
    "description": "Rich chocolate sorbet",
    "price": 52000,
    "category": "sorbet"
  }'
```

#### Submit Contact Message
```bash
curl -X POST http://localhost:5000/api/contact \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "message": "Love your products!"
  }'
```

## 🎯 Learning Objectives

This project helps beginners learn:

### Python API Development
- ✅ Creating REST APIs with Flask
- ✅ Handling HTTP methods (GET, POST)
- ✅ JSON data processing
- ✅ Error handling
- ✅ CORS configuration
- ✅ Request validation

### Web Development Concepts
- ✅ Frontend-backend communication
- ✅ API endpoints and routes
- ✅ HTTP status codes
- ✅ Data serialization (JSON)

## 📁 Project Structure

```
cream-shop-web/
├── app.py              # Main API application
├── run_server.py       # Easy server starter
├── api_examples.py     # API usage examples
├── requirements.txt    # Python dependencies
├── index.html         # Main website page
├── about.html         # About page
├── style.css          # Website styles
├── script.js          # Website JavaScript
├── image/             # Images for the website
└── README.md          # This file
```

## 🛠️ API Features

### Current Features
- ✅ Product management (CRUD operations)
- ✅ Shop information endpoint
- ✅ Contact form submission
- ✅ Category filtering
- ✅ Input validation
- ✅ CORS enabled for frontend integration
- ✅ Detailed error messages

### Sample Data Included
- 🥥 Coconut Sorbetto
- 🍊 Tequila Sunrise Sorbet
- 🥭 Mango Passion Sorbet

## 🔧 Customization Ideas

### For Beginners
1. **Add new products** to the sample data
2. **Create new endpoints** (e.g., `/api/favorites`)
3. **Add more fields** to products (nutrition info, allergens)
4. **Implement search functionality**

### For Intermediate
1. **Add a database** (SQLite, PostgreSQL)
2. **Implement user authentication**
3. **Add image upload for products**
4. **Create an admin dashboard**

## 🌐 Frontend Integration

The website can be enhanced to use the API:

```javascript
// Example: Fetch products from API
fetch('http://localhost:5000/api/products')
  .then(response => response.json())
  .then(data => {
    console.log('Products:', data.products);
    // Display products on website
  });
```

## 📚 Learning Resources

### Next Steps
- Learn about databases with SQLAlchemy
- Explore authentication with Flask-Login
- Try deployment with Heroku or Vercel
- Add testing with pytest

### Recommended Reading
- [Flask Documentation](https://flask.palletsprojects.com/)
- [REST API Design Best Practices](https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/)
- [HTTP Status Codes](https://httpstatuses.com/)

## 🤝 Contributing

This is a learning project! Feel free to:
- Add new features
- Improve documentation
- Fix bugs
- Share your improvements

## 📞 Support

If you're learning and need help:
1. Check the comments in `app.py` - they explain everything!
2. Run `api_examples.py` to see working examples
3. Use the browser's developer tools to inspect API calls

## 🎉 Success Tips

1. **Start the server first** before testing
2. **Read error messages carefully** - they help you learn
3. **Use a tool like Postman** for testing APIs
4. **Check the terminal** for server logs
5. **Experiment and have fun!**

---

**Happy coding! 🍧✨**

*Green Sorbetto - Where every API call is a work of art!*
