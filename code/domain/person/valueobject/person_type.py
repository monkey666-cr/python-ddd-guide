"""
Author: ChenRun
Date: 2022-02-25 22:36:09
Description: 
"""
from enum import Enum

class PersonType(str, Enum):
    INTERNAL = "INTERNAL"
    EXTERNAL = "EXTERNAL"