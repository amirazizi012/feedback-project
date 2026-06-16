from sqlalchemy.orm import Session
from . import models, schemas, auth

def create_initial_admin(db: Session):
    admin = db.query(models.User).filter(models.User.username == "admin").first()
    if not admin:
        hashed_pw = auth.get_password_hash("password123")
        new_admin = models.User(username="admin", hashed_password=hashed_pw)
        db.add(new_admin)
        db.commit()

def create_feedback(db: Session, feedback: schemas.FeedbackCreate):
    db_feedback = models.Feedback(title=feedback.title, message=feedback.message)
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

def get_feedbacks(db: Session):
    return db.query(models.Feedback).order_by(models.Feedback.created_at.desc()).all()

def update_feedback_status(db: Session, feedback_id: int, status: str):
    feedback = db.query(models.Feedback).filter(models.Feedback.id == feedback_id).first()
    if feedback:
        feedback.status = status
        db.commit()
        db.refresh(feedback)
    return feedback
