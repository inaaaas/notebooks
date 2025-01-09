from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from .database import Base

class Laptop(Base):
    __tablename__ = "laptops"
    id = Column(Integer, primary_key=True, index=True)
    model = Column(String, index=True)
    processor = Column(String)
    gpu = Column(String)
    screen_size = Column(Float)
    memory_size = Column(Integer)
    offers = relationship("MarketOffer", back_populates="laptop")

class Manufacturer(Base):
    __tablename__ = "manufacturers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    country = Column(String)
    location = Column(String)
    warranty = Column(Integer)
    offers = relationship("MarketOffer", back_populates="manufacturer")

class MarketOffer(Base):
    __tablename__ = "market_offers"
    id = Column(Integer, primary_key=True, index=True)
    batch_size = Column(Integer)
    price = Column(Float)
    date = Column(String)
    laptop_id = Column(Integer, ForeignKey("laptops.id"))
    manufacturer_id = Column(Integer, ForeignKey("manufacturers.id"))
    laptop = relationship("Laptop", back_populates="offers")
    manufacturer = relationship("Manufacturer", back_populates="offers")
