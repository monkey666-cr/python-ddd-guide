"""
Author: ChenRun
Date: 2022-02-25 22:31:09
Description: 
"""
from pydantic import BaseModel


class Relationship(BaseModel):
    id: str
    person_id: str
    leader_id: str
    leader_level: int
