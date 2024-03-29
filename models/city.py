#!/usr/bin/python3
"""City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """city.

    Attributes:
        state_id (str): state id.
        name (str): name of city.
    """

    state_id = ""
    name = ""
