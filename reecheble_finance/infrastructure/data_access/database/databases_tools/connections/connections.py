from pymongo import MongoClient

# Provide the connection details
hostname = 'your_host_name'
port = 27017  # Default MongoDB port
username = 'your_username'  # If authentication is required
password = 'your_password'  # If authentication is required

# Create a MongoClient instance
client = MongoClient(hostname, port, username=username, password=password)
