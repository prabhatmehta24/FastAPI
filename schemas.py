from pydantic import BaseModel
#input schema

class BlogCreate(BaseModel):
    title:str
    content:str

#output Schema
class BlogResponse(BaseModel):
    id:int
    title:str
    content:str