# Placeholder content for request_schemas.py
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# --------------------
# Request Schemas
# --------------------


class PowerRequest(BaseModel):
    base: int = Field(..., example=2, description="The base number")
    exp: int = Field(..., example=3, description="The exponent")


class FactorialRequest(BaseModel):
    n: int = Field(..., ge=0, example=5, description="Non-negative integer")


class FibonacciRequest(BaseModel):
    n: int = Field(..., ge=0, example=7, description="Index of Fibonacci sequence")

# --------------------
# Response Schema
# --------------------


class MathResponse(BaseModel):
    operation: str
    input_data: str
    result: float
    timestamp: Optional[datetime]
