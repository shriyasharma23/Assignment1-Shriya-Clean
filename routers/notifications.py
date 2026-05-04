from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, timezone
from database import get_db
from models import Device

router = APIRouter()


@router.get("/deviceConfigNotification")
def deviceConfigNotification(db: Session = Depends(get_db)):

    changed_devices = db.query(Device).filter(Device.config_changed == True).all()

    if not changed_devices:
        return {
            "status":  "ok",
            "message": "No configuration changes detected across any devices."
        }

    notifications = []
    for device in changed_devices:
        notifications.append({
            "notification_type": "CONFIG_CHANGE_ALERT",
            "device_id":         device.id,
            "device_ip":         device.device_ip,
            "device_details":    device.device_details,
            "message":           f"Configuration change detected on device {device.device_ip}",
            "timestamp":         datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        })

        device.config_changed = False

    db.commit()

    return {
        "status":              "alerts_sent",
        "total_notifications": len(notifications),
        "notifications":       notifications
    }