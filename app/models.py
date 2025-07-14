from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base  # ✅ This line is important!

class BogieChecksheet(Base):
    __tablename__ = "bogie_checksheet"
    id = Column(Integer, primary_key=True, index=True)
    adjusting_tube = Column(String)
    cylinder_body = Column(String)
    piston_trunnion = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class WheelSpecification(Base):
    __tablename__ = "wheel_specification"
    id = Column(Integer, primary_key=True, index=True)
    wheel_number = Column(String)
    condition = Column(String)
    inspected_by = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
