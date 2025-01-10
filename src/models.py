from pydantic import BaseModel
from pydantic import EmailStr, HttpUrl

class NLPDataInput(BaseModel):
    text: list[str]
    user_id: EmailStr

class ImageDataInput(BaseModel):
    url: list[HttpUrl]
    user_id: EmailStr

project = "End-to-End Machine Learning for Production"