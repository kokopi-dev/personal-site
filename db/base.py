#!/usr/bin/env python3
from sqlalchemy import Delete, ScalarResult, Select
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio.session import AsyncSession
from db.engine import async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from utils.env import Env
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import class_mapper


class Base(DeclarativeBase):
    def as_dict(self):
        mapper = class_mapper(self.__class__)
        columns = [column.key for column in mapper.columns]
        return {c: getattr(self, c) for c in columns}

class DatabaseConn:
    """Database connection class.
    The connection can execute, delete, and commit SQL queries.
    """
    engine: AsyncEngine = async_engine
    session: async_sessionmaker[AsyncSession]

    def __init__(self):
        self.session = async_sessionmaker(self.engine, expire_on_commit=False)

    async def execute(self, command: Select) -> ScalarResult:
        async with self.session() as conn:
            result = await conn.execute(command)
            return result.scalars()

    async def delete(self, command: Delete) -> None:
        async with self.session() as conn:
            await conn.execute(command)
            await conn.commit()

    async def commit(self, model) -> None:
        async with self.session() as conn:
            conn.add(model)
            await conn.commit()
            await conn.refresh(model)
