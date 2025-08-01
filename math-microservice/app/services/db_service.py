from sqlalchemy.orm import Session
from app.models.request_log import RequestLog
from datetime import datetime

def get_existing_log(db: Session, operation: str, input_data: str):
    return db.query(RequestLog).filter_by(operation=operation, input_data=input_data).first()

def save_log(db: Session, operation: str, input_data: str, result: float):
    log = RequestLog(
        operation=operation,
        input_data=input_data,
        result=result,
        timestamp=datetime.utcnow()
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return log
