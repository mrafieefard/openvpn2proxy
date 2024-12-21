from pydantic import BaseModel

class Config(BaseModel):
    name : str

class ConfigResponse(BaseModel):
    configs : list[Config]

class ActivePayload(BaseModel):
    name : str