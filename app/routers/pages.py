from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
import os

router = APIRouter(tags=["Frontend Pages"])

current_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
templates = Jinja2Templates(directory=os.path.join(current_dir, "templates"))

@router.get("/")
def read_index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@router.get("/dashboard")
def read_dashboard(request: Request):
    return templates.TemplateResponse(request=request, name="dashboard.html")
