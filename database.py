from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///bakery.db")
Base = declarative_base()

class Order(Base):
    """
    Order schema for the bakery

    Args:
        Base (declarative_base): SQLAlchemy Base DB model
    """
    __tablename__ = "order"
    id = Column(Integer, primary_key=True)
    order = Column(String(256))
    quantity = Column(Integer)
