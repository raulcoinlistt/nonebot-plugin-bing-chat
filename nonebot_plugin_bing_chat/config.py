from pydantic import BaseModel, Extra

class Config(BaseModel, extra=Extra.ignore):
    bingchat_output = 'text'