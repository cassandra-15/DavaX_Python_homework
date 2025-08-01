# Placeholder content for request_log.py
# app/models/request_log.py
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.database.session import Base
from sqlalchemy import UniqueConstraint

class RequestLog(Base):
    __tablename__ = "requests"
    __table_args__ = (UniqueConstraint('operation', 'input_data', name='_operation_input_uc'),)

    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String)
    input_data = Column(String)
    result = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
