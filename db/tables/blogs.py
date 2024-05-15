#!/usr/bin/env python3
from sqlalchemy import select
from db.models.blogs import PersonalBlogMetaModel
from db.tables.base import BaseTable
from sqlalchemy import func


class BlogTable(BaseTable):
    async def get_random_blog_meta(self) -> PersonalBlogMetaModel|None:
        query = select(PersonalBlogMetaModel).order_by(func.random())
        result = await self._conn.execute(query)
        if result:
            return result.first()
