from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for users
# Key = user_id (int), Value = dict with name & email
users = {}

# GET - Retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# GET - Retrieve a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id]), 200
    return jsonify({"error": "User not found"}), 404

# POST - Add a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or "id" not in data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    user_id = data["id"]
    if user_id in users:
        return jsonify({"error": "User already exists"}), 400
    
    users[user_id] = {"name": data["name"], "email": data["email"]}
    return jsonify({"message": "User created successfully"}), 201

# PUT - Update user details
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid input"}), 400
    
    users[user_id].update(data)
    return jsonify({"message": "User updated successfully"}), 200

# DELETE - Remove a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    
    del users[user_id]
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
