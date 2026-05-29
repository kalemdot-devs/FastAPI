from pydantic import BaseModel
import json, time

class RentalListing(BaseModel):
    id: int
    title: str
    price: float = 0
    sellerName: str
    agentName: str
    description: str