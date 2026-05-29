import json
from fastapi import FastAPI
from fastapi import File, UploadFile
from fastapi import Request
from models import RentalListing
from property_listings import *

app = FastAPI()
listings = get_listings()


@app.get("/")
async def home():
    return {"message": "Welcome to FastAPI"}

# Dynamic Route
@app.get('/items/{item_id}')
async def read_items(item_id: int):
    return {"item_id": item_id}

# Query Parameters
@app.get("/users")
async def get_user(name: str | None = None):
    return {"name": name}

# Opetional params
@app.get('/products')
async def get_products(limit:int = 10):
    return {
        "limit": limit
    }

# get property listings 
@app.get("/listings")
async def get_property_listings():
    return listings

# path parameters/params
@app.get("/listings/{offers}")
async def get_property_offers(offers: str):
    property_offers = listings[offers]
    return property_offers

# Query Params
@app.get('/listings/agent_info/{info}')
async def get_listing_agent_info(info: str):
    offered_by_agent = listings['offers']['offeredBy'][0].get(info, '')
    if offered_by_agent:
        return {
            "ListingAgentInfo": offered_by_agent
        }
    else:
        return {
            "ListingAgentInfo": "Not Available"
        }

# query params using request
@app.get('/listings/property_info/')
async def get_main_entity(request: Request):
    q = dict(request.query_params)
    mainEntity = q.get('mainEntity')
    if mainEntity:
        return {
            "property_info": listings[mainEntity]
        }
    else:
        return {
            "ERROR": "Key Error"
        }

# post method
@app.post('/create_listing')
async def create_rentals(body:RentalListing):
    rentals_data = body.model_dump()
    property_info.append(rentals_data)
    return {
        "status": "Listing Created Successfully...",
        "Listings": property_info
    }

# who we send data to the server 
# Body, headers -> request-headers, query -> query-params
