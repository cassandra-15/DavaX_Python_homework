from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from app.services.math_service import calculate_power, calculate_factorial, calculate_fibonacci
from app.services.cache import get_cached_result, set_cached_result
from app.database.session import get_db
from app.models.request_log import RequestLog
from app.schemas.request_schemas import MathResponse
from app.utils.logger import log_to_kafka

router = APIRouter()


def get_or_create_log(operation: str, input_data: str, compute_fn, db: Session) -> MathResponse:
    # Check cache
    cached = get_cached_result(operation, input_data)
    if cached is not None:
        # If cache hit, try to get the timestamp from DB
        log = db.query(RequestLog).filter_by(operation=operation, input_data=input_data).first()
        timestamp = log.timestamp if log else None  # fallback in case no DB entry
        return MathResponse(operation=operation, input_data=input_data, result=cached, timestamp=timestamp)

    # Check DB
    log = db.query(RequestLog).filter_by(operation=operation, input_data=input_data).first()
    if log:
        return MathResponse(operation=log.operation, input_data=log.input_data, result=log.result, timestamp=log.timestamp)

    # Compute fresh result
    result = compute_fn()
    set_cached_result(operation, input_data, result)
    log = RequestLog(operation=operation, input_data=input_data, result=result)
    db.add(log)
    db.commit()
    db.refresh(log)
    return MathResponse(operation=log.operation, input_data=log.input_data, result=log.result, timestamp=log.timestamp)


@router.get("/power", response_model=MathResponse)
def power(base: int, exp: int, db: Session = Depends(get_db)):
    input_data = f"{base}^{exp}"
    response = get_or_create_log("power", input_data, lambda: calculate_power(base, exp), db)
    log_to_kafka("api_requests", {
        "operation": "power",
        "input": input_data,
        "result": response.result,
        "source": "db" if response.timestamp else "cache"
    })
    return response


@router.get("/factorial", response_model=MathResponse)
def factorial(n: int, db: Session = Depends(get_db)):
    key = str(n)
    response = get_or_create_log("factorial", key, lambda: calculate_factorial(n), db)
    log_to_kafka("api_requests", {
        "operation": "factorial",
        "input": key,
        "result": response.result,
        "source": "db" if response.timestamp else "cache"
    })
    return response


@router.get("/fibonacci", response_model=MathResponse)
def fibonacci(n: int, db: Session = Depends(get_db)):
    key = str(n)
    response = get_or_create_log("fibonacci", key, lambda: calculate_fibonacci(n), db)
    log_to_kafka("api_requests", {
        "operation": "fibonacci",
        "input": key,
        "result": response.result,
        "source": "db" if response.timestamp else "cache"
    })
    return response
