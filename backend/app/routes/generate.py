from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..services.generator_service import generate_campaign
from ..database import get_db

router = APIRouter()

@router.post("/generate")
def generate_content(product_id: int, db: Session = Depends(get_db)):
    try:
        return generate_campaign(product_id, db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))