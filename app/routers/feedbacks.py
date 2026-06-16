from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas, crud
from ..dependencies import get_db, get_current_user

router = APIRouter(prefix="/api/feedbacks", tags=["Feedbacks"])

@router.post("", response_model=schemas.FeedbackResponse, status_code=status.HTTP_201_CREATED)
def submit_feedback(feedback: schemas.FeedbackCreate, db: Session = Depends(get_db)):
    return crud.create_feedback(db, feedback)

@router.get("", response_model=list[schemas.FeedbackResponse])
def get_all_feedbacks(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    return crud.get_feedbacks(db)

@router.patch("/{feedback_id}", response_model=schemas.FeedbackResponse)
def update_status(feedback_id: int, feedback_update: schemas.FeedbackUpdate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    valid_statuses = ['ثبت شده', 'در حال بررسی', 'رسیدگی شده']
    if feedback_update.status not in valid_statuses:
        raise HTTPException(status_code=400, detail="وضعیت نامعتبر است")
    
    updated_feedback = crud.update_feedback_status(db, feedback_id, feedback_update.status)
    if not updated_feedback:
        raise HTTPException(status_code=404, detail="فیدبک پیدا نشد")
    return updated_feedback
