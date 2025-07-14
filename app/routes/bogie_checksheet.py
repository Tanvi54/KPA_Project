from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, models, schemas
from datetime import datetime

router = APIRouter(prefix="/api/forms", tags=["Bogie Checksheet"])

@router.post("/bogie-checksheet", response_model=schemas.BogieChecksheetOut)
def create_checksheet(data: schemas.BogieChecksheetIn, db: Session = Depends(database.get_db)):
    record = models.BogieChecksheet(
        adjusting_tube=data.adjusting_tube,
        cylinder_body=data.cylinder_body,
        piston_trunnion=data.piston_trunnion,
        created_at=datetime.utcnow()
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record
