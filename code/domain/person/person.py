"""
Author: ChenRun
Date: 2022-02-25 22:31:01
Description: 
"""
from datetime import datetime
from typing import List
from pydantic import BaseModel

from .relation_ship import Relationship
from .valueobject.person_type import PersonType
from .valueobject.person_status import PersonStatus


class Person(BaseModel):
    person_id: str
    person_name: str
    person_type: PersonType
    relationships: List[Relationship]
    role_level: int
    create_time: datetime
    last_modify_time: datetime
    status: PersonStatus


    def create(self) -> "Person":
        self.create_time = datetime.now()
        self.status = PersonStatus.ENABLE
        return self

    def enable(self) -> "Person":
        self.last_modify_time = datetime.now()
        self.status = PersonStatus.ENABLE
        return self

    def disable(self) -> "Person":
        self.last_modify_time = datetime.now()
        self.status = PersonStatus.DISABLE
        return self
