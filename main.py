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

@app.get('/property/info/{id}')
async def get_listing_info_by_id(id: int):
    return {
        "RentalsInfo of ID": property_info[id]
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

# Update product Rentals data
@app.put('/update_listing/{listing_id}')
def update_listing(listing_data:RentalListing, listing_id:int):
    for index, props_data in enumerate(property_info, start=1):
        if props_data.get('id') == listing_id:
            property_info[index] = listing_data.model_dump()
            return {
                "status": "Listing Updated Successfully...",
                "ListingData": listing_data
            }    
        # print(f'{index}: {props_data}')

        return {
            "ERROR": "Property Listing Not found for this ID"
        }

@app.delete('delete_listing/{listing_id}')
async def delete_listing(listing_id: int):
    for index, props_data in enumerate(property_info):
        if props_data.get('id') == listing_id:
            removed_listing = property_info.pop(index)
            return {
                "status": "Property Listing Deleted Successfully...",
                "Deleted Listing": removed_listing
            }
    return {"Error": "Property Listing for this ID not Exist"}

# how we send data to the server 
# Body, headers -> request-headers, query -> query-params
