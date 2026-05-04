from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime
from database import get_db
from models import Inventory, InventoryDetails

router = APIRouter()


@router.get("/getInventoryDetails")
def getInventoryDetails(
    start_date: str,
    end_date: str,
    db: Session = Depends(get_db)
):
    try:
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end   = datetime.strptime(end_date,   "%Y-%m-%d")
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail="Invalid date format. Use YYYY-MM-DD"
        )

    if start > end:
        raise HTTPException(
            status_code=400,
            detail="start_date cannot be after end_date"
        )

    results = (
        db.query(Inventory, InventoryDetails)
        .join(InventoryDetails, Inventory.id == InventoryDetails.inventory_id)
        .filter(
            Inventory.purchase_dt >= start,
            Inventory.purchase_dt <= end
        )
        .all()
    )

    if not results:
        raise HTTPException(
            status_code=404,
            detail=f"No inventory records found between {start_date} and {end_date}"
        )

    inventory_list = [
        {
            "inventory_id":  inv.id,
            "purchase_date": inv.purchase_dt.strftime("%Y-%m-%d"),
            "cost":          inv.cost,
            "details":       det.inventory_details
        }
        for inv, det in results
    ]

    return {
        "status":           "success",
        "start_date":       start_date,
        "end_date":         end_date,
        "total_records":    len(inventory_list),
        "inventoryDetails": inventory_list
    }