from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from sqlalchemy.orm import Session

from database import Base, Order, engine

Base.metadata.create_all(engine)
app = FastAPI()

price_list = {
    "small_bread": 5,
    "small_buns": 1,
    "small_cake": 10,
    "medium_bread": 10,
    "medium_buns": 2,
    "medium_cake": 20,
    "large_bread": 15,
    "large_buns": 3,
    "large_cake": 30,
}

class OrderRequest(BaseModel):
    """
    Pydantic data model for order api call
    """
    order: str
    quantity: int

@app.post("/order/", status_code=status.HTTP_201_CREATED)
def create_order(order: OrderRequest):
    """Create new baking order and store for reuse

    Returns:
        str: Created order details
    """
    session = Session(bind=engine, expire_on_commit=False)
    orderdb = Order(order = order.order, quantity = order.quantity)
    session.add(orderdb)
    session.commit()
    ID = orderdb.id
    session.close()
    return f"Baking order created with id {ID}"


@app.get("/orders")
def get_orders():
    """Create new baking order and store for reuse

    Returns:
        str: Created order details
    """
    session = Session(bind=engine, expire_on_commit=False)
    orders = session.query(Order).all()
    session.close()
    return orders

@app.get("/orders/{ID}")
def get_order(ID: int):
    """Fetch specific order item

    Args:
        ID (int): Order ID

    Returns:
        str: Order details
    """
    session = Session(bind=engine, expire_on_commit=False)
    order = session.query(Order).get(ID)
    session.close()
    if not order:
        raise HTTPException(status_code=404, detail=f"Order with id {ID} not found")
    return f"Order with id: {order.id} and quantity: {order.quantity} available"

@app.put("/orders/{ID}")
def update_order(ID: int, order: str, quantity: int):
    """Fetch specific order item

    Args:
        ID (int): Order ID
        Order: Updated order details
        Quantity: Updated order quantity

    Returns:
        str: Order details
    """
    session = Session(bind=engine, expire_on_commit=False)
    if dborder := session.query(Order).get(ID):
        dborder.order = order
        dborder.quantity = quantity
        session.commit()
    session.close()
    if not dborder:
        raise HTTPException(status_code=404, detail=f"Order with ID {ID} not found")
    return dborder

@app.delete("/orders/{ID}", status_code=status.HTTP_204_NO_CONTENT)
def delete_order(ID: int):
    """Fetch specific order item

    Args:
        ID (int): Order ID

    Returns:
        str: Order details
    """
    session = Session(bind=engine, expire_on_commit=False)
    
    if not (dborder := session.query(Order).get(ID)):
        raise HTTPException(status_code=404, detail=f"Order with id: {ID} not found")
    session.delete(dborder)
    session.commit()
    session.close()
    return None


# def payment(order):
#     pass

# def delivery(order):
#     pass

# def bake(order):
#     pass


@app.get("/")
def root():
    """Base or root path for bakesalot"""
    return {"message": "Welcome to the Bakes-a-lot"}


@app.get("/prices")
def prices():
    """Show price list of all bakery items"""
    return {"prices": price_list}
