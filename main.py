from fastapi import FastAPI

app = FastAPI()

# class BakedItem:
#     """Base class for any item in the bakery
#     """
#     def __init__(self, name: str, size: str) -> None:
#         """Every item in the bakery has a name and size

#         Args:
#             name (str): Name of the baked goods e.g. bread, buns, cake, etc
#             size (str): Size of item ordered, e.g. small, medium, large
#         """
#         self.name = name
#         self.size = size
    
#     def get_bake_item(self):
#         return f"{self.name, self.size}"
        
price_list = {
    "small_bread": 5,
    "small_buns": 1,
    "small_cake": 10,
    "medium_bread": 10,
    "medium_buns": 2,
    "medium_cake": 20,
    "large_bread": 15,
    "large_buns": 3,
    "large_cake": 30
}

@app.post("/order/")
def create_order():
    """Create new baking order and store for reuse

    Returns:
        str: Created order details
    """
    return {"message": "Baking order created"}

@app.get("/orders")
def get_orders():
    """Create new baking order and store for reuse

    Returns:
        str: Created order details
    """
    return {"message": "Fetched all orders"}

@app.get("/orders/{id}")
def get_orders(id: int):
    """Fetch specific order item

    Args:
        id (int): Order ID

    Returns:
        str: Order details
    """
    return {"message": "Fetch order"}

# def payment(order):
#     pass

# def delivery(order):
#     pass

# def bake(order):
#     pass

@app.get("/")
def root():
    """Base or root path for bakesalot
    """
    return {"message": "Welcome to the Bakes-a-lot"}

@app.get("/prices")
def prices():
    """Show price list of all bakery items
    """
    return {"prices": price_list}

def main():
    pass


if __name__ == "__main__":
    main()
