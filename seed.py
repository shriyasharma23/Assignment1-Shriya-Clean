from datetime import datetime
from database import SessionLocal, engine
from models import Base, Inventory, InventoryDetails, Device, Post

def seed():
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    try:
        if db.query(Inventory).count() == 0:
            inv1 = Inventory(purchase_dt=datetime(2025, 2, 14), cost=1500.00)
            inv2 = Inventory(purchase_dt=datetime(2025, 6, 20), cost=3200.00)
            inv3 = Inventory(purchase_dt=datetime(2024, 11, 5), cost=800.00)
            db.add_all([inv1, inv2, inv3])
            db.flush()

            db.add(InventoryDetails(inventory_id=inv1.id, inventory_details="Dell XPS 15 Laptop"))
            db.add(InventoryDetails(inventory_id=inv2.id, inventory_details="HP ProLiant Server Rack"))
            db.add(InventoryDetails(inventory_id=inv3.id, inventory_details="Cisco Network Switch"))
            print("Q1: Inventory data seeded")

        if db.query(Device).count() == 0:
            db.add(Device(device_ip="192.168.1.1",  device_details="Main Router",   config_changed=True))
            db.add(Device(device_ip="192.168.1.2",  device_details="Backup Switch", config_changed=True))
            db.add(Device(device_ip="192.168.1.10", device_details="Access Point",  config_changed=False))
            print("Q2: Device data seeded")

        if db.query(Post).count() == 0:
            for i in range(1, 31):
                db.add(Post(
                    post_by=f"user_{i}",
                    post_dt=datetime(2025, (i % 12) + 1, (i % 28) + 1),
                    post_details=f"This is sample post number {i}."
                ))
            print("Q3: Posts data seeded (30 posts)")

        db.commit()
        print("Database seeded successfully!")

    except Exception as e:
        db.rollback()
        print(f"Error seeding data: {e}")
    finally:
        db.close()


if __name__ == "__main__":
    seed()