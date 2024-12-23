from pydantic import BaseModel, UUID4



class DescriptionModel(BaseModel):
    terror_attack_id : UUID4
    description: str