"""
Author: ChenRun
Date: 2022-02-25 22:43:09
Description: 
"""
from enum import Enum


class PersonStatus(str, Enum):
    ENABLE = "ENABLE"
    DISABLE = "DISABLE"
