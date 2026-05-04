from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Inventory(Base):
    __tablename__ = "inventory"

    id          = Column(Integer, primary_key=True, index=True)
    purchase_dt = Column(DateTime, nullable=False)
    cost        = Column(Float, nullable=False)

    details = relationship("InventoryDetails", back_populates="inventory")


class InventoryDetails(Base):
    __tablename__ = "inventory_details"

    id                = Column(Integer, primary_key=True, index=True)
    inventory_id      = Column(Integer, ForeignKey("inventory.id"), nullable=False)
    inventory_details = Column(String, nullable=False)

    inventory = relationship("Inventory", back_populates="details")


class Device(Base):
    __tablename__ = "devices"

    id             = Column(Integer, primary_key=True, index=True)
    device_ip      = Column(String, nullable=False)
    device_details = Column(String)
    config_changed = Column(Boolean, default=False)


class Post(Base):
    __tablename__ = "posts"

    id           = Column(Integer, primary_key=True, index=True)
    post_by      = Column(String, nullable=False)
    post_dt      = Column(DateTime, nullable=False)
    post_details = Column(String)