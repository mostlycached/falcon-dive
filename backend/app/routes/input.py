from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, models
from ..database import get_db, engine, Base

# Ensure database tables are created
Base.metadata.create_all(bind=engine)

router = APIRouter()



@router.post("/input", response_model=schemas.InputDataCreate)
def store_input(data: schemas.InputDataCreate, db: Session = Depends(get_db)):
    # Save data to the database
    db_data = crud.create_input_data(db, data)

    return db_data


@router.get("/input", response_model=List[schemas.InputDataCreate])
def get_all_input_data(db: Session = Depends(get_db)):
    # Query all records from the database
    data = db.query(models.InputData).all()

    # Convert SQLAlchemy objects to Pydantic models
    return [schemas.InputDataCreate.from_orm(record) for record in data]
