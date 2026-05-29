import os, time, sys
import json

def get_listings():
    with open('props_listing.json', 'r', encoding='utf-8') as f:
        rentals_data = json.load(f)
    return rentals_data


property_info = [
    {
        "id": 1,
        "title": "2917 Dellinger Dr, Charlotte, NC 28269",
        "price": 319000,
        "sellerName": "Moss Realty",
        "agentName": "Greg Holland",
        "potentialAction": "BuyAction",
        "description": "Welcome to 2917 Dellinger Dr, this is a great 1 level home offering a split bedroom floor plan. The kitchen has updated appliances, great cabinet, and counter space. The primary suite has a private bath that was updated in approx 2023, and also offers great closet space. Other updates include all new interior doors in 2025 as well as new carpet in bedrooms in 2025. All windows were replaced in 2021. Outside, you will find a nice level lot, a patio, and a 6' privacy fence in the backyard. The home is conveniently located approx 15 minutes to uptown and also has easy access to a CATS stop just outside the neighborhood. Listing Agent related to Seller. Professional photos coming soon."
    },
    {
        "id": 2,
        "title": "2918 Dellinger Dr, Charlotte, NC 28269",
        "price": 319001,
        "sellerName": "Moss Realty Inc",
        "agentName": "Greg visa",
        "potentialAction": "BuyAction",
        "description": "Welcome to 2918 Dellinger Dr, this is a great 1 level home offering a split bedroom floor plan. The kitchen has updated appliances, great cabinet, and counter space. The primary suite has a private bath that was updated in approx 2023, and also offers great closet space. Other updates include all new interior doors in 2025 as well as new carpet in bedrooms in 2025. All windows were replaced in 2021. Outside, you will find a nice level lot, a patio, and a 6' privacy fence in the backyard. The home is conveniently located approx 15 minutes to uptown and also has easy access to a CATS stop just outside the neighborhood. Listing Agent related to Seller. Professional photos coming soon."
    },
    {
        "id": 3,
        "title": "2919 Dellinger Dr, Charlotte, NC 28269",
        "price": 319002,
        "sellerName": "Rightmove Realty",
        "agentName": "Mark Hill",
        "potentialAction": "BuyAction",
        "description": "Welcome to 2919 Dellinger Dr, this is a great 1 level home offering a split bedroom floor plan. The kitchen has updated appliances, great cabinet, and counter space. The primary suite has a private bath that was updated in approx 2023, and also offers great closet space. Other updates include all new interior doors in 2025 as well as new carpet in bedrooms in 2025. All windows were replaced in 2021. Outside, you will find a nice level lot, a patio, and a 6' privacy fence in the backyard. The home is conveniently located approx 15 minutes to uptown and also has easy access to a CATS stop just outside the neighborhood. Listing Agent related to Seller. Professional photos coming soon."
    },

]
