#!/usr/bin/env python3
from pydantic import BaseModel

class Experience(BaseModel):
    company: str
    time: str
    title: str
    location: str
    description: str
    work_style: str
    tech: list[str] = []

class Experiences(BaseModel):
    items: list[Experience] = [
        Experience(
            company="Westbold",
            time="Jul 2021 - Present",
            title="Full Stack Software Engineer",
            location="Vancouver, Washington, United States",
            description="C# - ASP.NET Blazor Server w/ Tailwindcss & Vanilla Javascript, and Golang Hugo.",
            work_style="Remote",
            tech=["C#", "Blazor", "Tailwindcss", "Hugo", "Javascript", "Python"]
        ),
        Experience(
            company="Tenchijin",
            time="Dec 2020 - Sep 2021",
            title="Full Stack Software Engineer",
            location="Tokyo, Japan",
            description="Python Django & VueJS - Backend lead/consultant",
            work_style="Remote",
            tech=["Python", "Django", "VueJS"]
        ),
        Experience(
            company="Hennge",
            time="Sep 2020 - Nov 2020",
            title="Intern Software Engineer",
            location="Tokyo, Japan",
            description="Internship",
            work_style="Intern",
            tech=["Python", "VueJS", "Terraform", "AWS"]
        ),
    ]

