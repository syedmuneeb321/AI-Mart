from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime,timedelta,timezone
from typing import List,Optional
import enum
from uuid import UUID,uuid4
from sqlalchemy import text


class PaymentMethod(str,enum.Enum):
    cod = "cod"
    card = "card"


class PaymentStatus(str,enum.Enum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class BasePayment(SQLModel):
    order_id: int 
    amount: float 
    payment_method: PaymentMethod 
    card_number: str|None = None 
    card_date: str | None = None 
    card_cvv: str | None = None



class Payment(BasePayment,table=True):
    id: UUID | None = Field(default_factory=uuid4,primary_key=True,nullable=False)
    customer_id: int
    payment_status: PaymentStatus = Field(default=PaymentStatus.PENDING)
    transaction_id: str | None = None
    created_at: datetime | None = Field(default_factory=datetime.now)
    updated_at: datetime | None = Field(default_factory=datetime.now)

    # class Config:
    #     json_encoders = {
    #         UUID: lambda v: str(v)
    #     }

class PaymentCreate(BasePayment):
    pass

class PaymentPublic(BasePayment):
    id: UUID
