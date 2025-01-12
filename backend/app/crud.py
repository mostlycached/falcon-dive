from sqlalchemy.orm import Session
from . import models, schemas

def create_input_data(db: Session, data: schemas.InputDataCreate):
    db_data = models.InputData(
        product_name=data.product_name,
        product_description=data.product_description,
        target_audience=data.target_audience,
        brand_tone=data.brand_tone,
        competitors=data.competitors,
    )
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data