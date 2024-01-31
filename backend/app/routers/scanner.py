from typing import Any
from fastapi import APIRouter
import requests
from bs4 import BeautifulSoup

router = APIRouter()

@router.post("/scan-web")
async def test_token(html_content: str) -> Any:
    soup = BeautifulSoup(html_content, 'html.parser')

    product_title = soup.find('h1', class_='product-title').text.strip()
    price = soup.find('span', class_='product-price').text.strip()
    description = soup.find('div', class_='product-description').text.strip()

    # Print or return the extracted information
    print(f"Product Title: {product_title}")
    print(f"Price: {price}")
    print(f"Description: {description}")
    
    # Return the information
    return {
        "name": "The name of the product",
        "price": "The price of the product",
        "image": "The image of the product",
        "description": "The description of the product",
        "url": "The url of the product"
    }

    
    