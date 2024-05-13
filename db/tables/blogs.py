#!/usr/bin/env python3
from sqlalchemy import select
from db.base import DatabaseConn
from db.models.blogs import PersonalBlogMetaModel
from sqlalchemy import func


class BlogTable:
    def __init__(self):
        self._conn = DatabaseConn()

    async def get_random_blog_meta(self) -> PersonalBlogMetaModel|None:
        query = select(PersonalBlogMetaModel).order_by(func.random())
        result = await self._conn.execute(query)
        return result.first()
