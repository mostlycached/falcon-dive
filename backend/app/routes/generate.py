from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from ..services.generator_service import generate_campaign
from ..database import get_db

router = APIRouter()

@router.get("/generate")
async def generate(
    product_id: int,
    use_dummy: bool = Query(False, description="Use dummy data instead of calling the LLM"),
    db: Session = Depends(get_db),
):
    """Generate campaign recommendations."""
    try:
        recommendations = generate_campaign(product_id, db, use_dummy)
        return {"recommendations": recommendations}
    except ValueError as e:
        return {"detail": str(e)}