from turtle import position, title
from flask import Flask, request, jsonify
app = Flask(__name__)
users = [
    {"name": 'john ', "position": "admin", "category": "staff"},
    {"name": 'doe', "position": "intern", "category": "intern"},
    {"name": 'adam', "position": "project manager", "category": "staff"},
    {"name": 'adam', "position": "project manager", "category": "auth"}
]
products = [
    {"title": 1, "description": "Thailand", "category": "Bangkok", "price": 513120,"available quantity": 513120, "date created": 513120, "date updated": 513120},
    {"title": 1, "description": "Thailand", "category": "Bangkok", "price": 513120,"available quantity": 513120, "date created": 513120, "date updated": 513120},
    {"title": 1, "description": "Thailand", "category": "Bangkok", "price": 513120,"available quantity": 513120, "date created": 513120, "date updated": 513120}
]
cart = []
# create users
@app.post("/users")
def create_users():
    if users['position']=='admin':
        users.append({"name": 'eve', "position": "project manager", "category": "staff"}
)
    return {"error": "only admin can update"}, 400

# create admin        
@app.post("/admin")
def create_admin():
    if users['position']=='admin':
        users.append({"name": 'steve', "position": "admin", "category": "staff"}
)
    return {"error": "only admin can update"}, 400

# create products
@app.post("/products")
def create_product():
    if users['position']=='admin':
        products.append({"title": 1, "description": "Thailand", "category": "Bangkok", "price": 513120,"available quantity": 513120, "date created": 513120, "date updated": 513120}
)
    return {"error": "only admin can create products"}, 400

# update products
@app.patch("/products")
def update_product():
    if users['position']=='admin':
        products.append({"title": 1, "description": "Thailand", "category": "Bangkok", "price": 513120,"available quantity": 513120, "date created": 513120, "date updated": 513120}
)
    return {"error": "only admin can update products"}, 400

# delete products
@app.delete("/products")
def delete_product():
    if users['position']=='admin':
        products.pop({"title": 1, "description": "Thailand", "category": "Bangkok", "price": 513120,"available quantity": 513120, "date created": 513120, "date updated": 513120}
)
    return {"error": "only admin can delete products"}, 400

# view products
@app.get("/products")
def view_product():
    for user in users:
        if user:
            return products[title]
        return {"error": "only users can view products"}, 400
    
# view by category
@app.get("/products/category_id")
def view_product(category):
    for user in users:
        if user:
            return products[category]
        return {"error": "only admin can view products"}, 400
    
    
# purchase products
@app.get("/products/category_id")
def view_product(category):
    for user in users:
        if user[category]== 'auth':
            cart.append(products[title])
            return cart
        return {"error": "only authorized users can purchase products"}, 400
