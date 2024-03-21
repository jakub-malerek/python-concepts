from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 175.50
            }
        ]
    }
]

@app.get("/stores")
def get_stores():
    return {"store":stores}


@app.post("/stores")
def post_stores():
    data = request.get_json()
    new_store = {"name":data["name"],"items":[]}
    stores.append(new_store)
    return new_store, 201    

@app.post("/stores/<string:name>/item")
def post_items(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_data = {"name":request_data["name"],"price":request_data["price"]}
            store["items"].append(new_data)
            return new_data, 201
    return {"message":"Store not found"}, 404    
