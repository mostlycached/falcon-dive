from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, models
from ..database import SessionLocal, engine

# Ensure database tables are created
models.Base.metadata.create_all(bind=engine)

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/input", response_model=schemas.InputDataCreate)
def store_input(data: schemas.InputDataCreate, db: Session = Depends(get_db)):
    # Save data to the database
    db_data = crud.create_input_data(db, data)

    # Convert SQLAlchemy model to Pydantic schema
    return schemas.InputDataCreate(
        product_name=db_data.product_name,
        product_description=db_data.product_description,
        target_audience=db_data.target_audience,
        brand_tone=db_data.brand_tone,
        competitors=db_data.competitors,
    )