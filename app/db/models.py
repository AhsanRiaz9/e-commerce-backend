from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    category = Column(String, index=True)
    price = Column(Float)

    # Establish one-to-many relationship with Sale model
    sales = relationship("Sale", back_populates="product")
    # Establish one-to-one relationship with Sale model
    inventory = relationship("Inventory", back_populates="product")


class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'), index=True)
    quantity = Column(Integer)
    date = Column(DateTime, default=datetime.datetime.utcnow)

    # Establish many-to-one relationship with Product model
    product = relationship("Product", back_populates="sales")

class Inventory(Base):
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'), index=True)
    quantity = Column(Integer)
    last_updated = Column(DateTime, default=datetime.datetime.utcnow)

    # Establish many-to-one relationship with Product model
    product = relationship("Product", back_populates="inventory")
