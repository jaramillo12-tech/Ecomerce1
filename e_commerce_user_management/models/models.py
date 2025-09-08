from typing import TypedDict


class Product(TypedDict):
    id: str
    name: str
    description: str
    price: float
    image_url: str
    category: str
    stock: int


class CartItem(TypedDict):
    product_id: str
    name: str
    price: float
    quantity: int
    image_url: str