from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import database, models, schemas

router = APIRouter(prefix="/api/forms", tags=["Wheel Specifications"])

@router.get("/wheel-specifications", response_model=list[schemas.WheelSpecificationOut])
def get_all_wheel_specs(db: Session = Depends(database.get_db)):
    specs = db.query(models.WheelSpecification).all()
    return specs
