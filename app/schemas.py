from pydantic import BaseModel

class VesselBase(BaseModel):
    name: str
    imo_number: str
    latitude: float
    longitude: float
    speed: float
    course: float

class VesselCreate(VesselBase):
    pass

class Vessel(VesselBase):
    id: int

    class Config:
        orm_mode = True
