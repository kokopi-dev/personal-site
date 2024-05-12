#!/usr/bin/env python3
"""Get a random coding blog from public folder"""
from db.tables.blogs import BlogTable
from pathlib import Path
from utils.env import Env
from selectolax.lexbor import LexborHTMLParser
import random

async def get_random_coding_blog_meta():
    meta = {}
    table = BlogTable()
    blogs = await table.get_blogs_by_code_category(Env.CODE_CATEGORY_ID)
    random_idx = random.randint(0, len(blogs) - 1)
    random_blog = blogs[random_idx]
    path = Path(Env.PUBLIC_BLOGS_FOLDER)
    blog_path = path / random_blog.category.name / random_blog.filename / "index.html"
    if blog_path.is_file():
        with blog_path.open("r", encoding="utf-8") as f:
            parser = LexborHTMLParser(f.read())
            head = parser.head
            if head:
                image = head.css('meta[name="og:image"]')[0].attributes.get("content")
                title = head.css('meta[name="og:title"]')[0].attributes.get("content")
                description = head.css('meta[name="og:description"]')[0].attributes.get("content")
                meta = {"image": image, "title": title, "description": description}
    return meta
