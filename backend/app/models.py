from sqlalchemy import Column, Integer, String, Text
from .database import Base

class InputData(Base):
    __tablename__ = "input_data"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    product_description = Column(Text)
    target_audience = Column(String)
    brand_tone = Column(String)
    competitors = Column(String)