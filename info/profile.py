#!/usr/bin/env python3
from pydantic import BaseModel

class Profile(BaseModel):
    name: str = "Derrick Gee"
    profession: str = "Full Stack Software Engineer"
    subtitle: str = "US Citizen living in Japan"
    description: str = "I like web development and learning new technologies that have real world application."
