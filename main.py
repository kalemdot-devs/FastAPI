import json
from fastapi import FastAPI
from fastapi import File, UploadFile

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to FastAPI"}

# Dynamic Route
@app.get('/items/{item_id}')
async def read_items(item_id: int):
    return {"item_id": item_id}


# Query Parameters
@app.get("/users/")
async def get_user(name: str = None):
    return {"user_name": name}

# Opetional params
@app.get('/products')
async def get_products(limit:int = 10):
    return {
        "limit": limit
    }

# Reading Json file show data on web json form
@app.get("/listings/")
async def get_property_listings():
    with open("props_listing.json", 'r', encoding='utf-8') as file:
        property_listings = json.load(file)
    return property_listings

@app.get("/listings/offers/")
async def get_property_offers():
    with open("props_listing.json", 'r', encoding='utf-8') as file:
        property_offers = json.load(file)
        property_offers = property_offers['offers']
    return property_offers