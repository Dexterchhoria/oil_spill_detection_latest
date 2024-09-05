from sqlalchemy.orm import Session
from .models import AISData
from .schemas import VesselCreate

def create_vessel(db: Session, vessel: VesselCreate):
    db_vessel = AISData(
        mmsi=vessel.mmsi,
        base_date_time=vessel.base_date_time,
        latitude=vessel.latitude,
        longitude=vessel.longitude,
        sog=vessel.sog,
        cog=vessel.cog,
        heading=vessel.heading,
        vessel_name=vessel.vessel_name,
        imo=vessel.imo,
        call_sign=vessel.call_sign,
        vessel_type=vessel.vessel_type,
        status=vessel.status,
        length=vessel.length,
        width=vessel.width,
        draft=vessel.draft,
        cargo=vessel.cargo,
        transceiver_class=vessel.transceiver_class
    )
    db.add(db_vessel)
    db.commit()
    db.refresh(db_vessel)
    return db_vessel

def get_vessel(db: Session, vessel_id: int):
    return db.query(AISData).filter(AISData.id == vessel_id).first()
