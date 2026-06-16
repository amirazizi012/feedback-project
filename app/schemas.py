from pydantic import BaseModel, Field
from datetime import datetime

class FeedbackCreate(BaseModel):
    title: str = Field(..., min_length=1)
    message: str = Field(..., min_length=1)

class FeedbackUpdate(BaseModel):
    status: str

class FeedbackResponse(BaseModel):
    id: int
    title: str
    message: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
