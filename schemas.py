from pydantic import BaseModel

class auth(BaseModel):
    api_key: str
    api_secret : str
