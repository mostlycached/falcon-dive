from pydantic import BaseModel

class InputDataCreate(BaseModel):
    product_name: str
    product_description: str
    target_audience: str
    brand_tone: str
    competitors: str