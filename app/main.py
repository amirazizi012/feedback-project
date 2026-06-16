from fastapi import FastAPI
from .database import engine, SessionLocal
from . import models, crud
from .routers import auth, feedbacks, pages

# ساخت جداول دیتابیس در همان ابتدای برنامه
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="سیستم فیدبک")

@app.on_event("startup")
def on_startup():
    db = SessionLocal()
    crud.create_initial_admin(db)
    db.close()

# اتصال روت‌های ماژولار به بدنه اصلی اپلیکیشن
app.include_router(pages.router)
app.include_router(auth.router)
app.include_router(feedbacks.router)
