"""
Easy Server Starter for Beginners
=================================

This file makes it super easy to start the API server.
Just run: python run_server.py
"""

import os
import sys

def check_requirements():
    """Check if required packages are installed"""
    try:
        import flask
        import flask_cors
        print("✅ All required packages are installed!")
        return True
    except ImportError as e:
        print("❌ Missing required packages!")
        print("Please install them with: pip install -r requirements.txt")
        return False

def main():
    """Start the server"""
    print("🍧 Green Sorbetto API Server Starter")
    print("="*40)
    
    # Check if requirements are installed
    if not check_requirements():
        sys.exit(1)
    
    print("🚀 Starting the API server...")
    print("📖 Once started, visit http://localhost:5000 for API info")
    print("🔍 Check api_examples.py to see how to use the API")
    print("⏹️  Press Ctrl+C to stop the server")
    print("="*40)
    
    # Import and run the app
    from app import app
    app.run(host='0.0.0.0', port=5000, debug=True)

if __name__ == "__main__":
    main()