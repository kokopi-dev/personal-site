#!/usr/bin/env python3
from typing import Sequence
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from db.base import DatabaseConn
from db.models.blogs import Blog, BlogCategory


class BlogTable:
    def __init__(self):
        self._conn = DatabaseConn()

    async def get_blogs_by_code_category(self, category_id) -> Sequence[Blog]:
        query = (select(Blog).where(Blog.category_id == category_id)
            .options(selectinload(Blog.category))
        )
        result = await self._conn.execute(query)
        return result.all()
