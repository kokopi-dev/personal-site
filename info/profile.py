#!/usr/bin/env python3
from pydantic import BaseModel
from enum import Enum

class SocialEnum(Enum):
    github = 0
    linkedin = 1

class Social(BaseModel):
    name: SocialEnum
    display_name: str
    url: str

class Profile(BaseModel):
    name: str = "Derrick Gee"
    profession: str = "Full Stack Software Engineer"
    subtitle: str = "US Citizen living in Japan"
    description: str = "I like web development and learning new technologies that have real world application."
    socials: list[Social] = [
        Social(name=SocialEnum.github, display_name="Github", url="https://github.com/kokopi-dev"),
        Social(name=SocialEnum.linkedin, display_name="Linkedin", url="https://www.linkedin.com/in/derrick-gee/")
    ]
