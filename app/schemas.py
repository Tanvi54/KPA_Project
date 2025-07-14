from pydantic import BaseModel
from datetime import datetime

# --- Input schema for POST request ---
class BogieChecksheetIn(BaseModel):
    adjusting_tube: str
    cylinder_body: str
    piston_trunnion: str

# --- Output schema for response ---
class BogieChecksheetOut(BogieChecksheetIn):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class WheelSpecificationOut(BaseModel):
    id: int
    wheel_number: str
    condition: str
    inspected_by: str
    created_at: datetime

    class Config:
        orm_mode = True
