from pydantic import BaseModel
from typing import List


class ParseRequest(BaseModel):
    source_code: str


class ParsedClass(BaseModel):
    name: str
    attributes: List[str]
    methods: List[str]


class ParseResponse(BaseModel):
    classes: List[ParsedClass]