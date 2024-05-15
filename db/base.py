#!/usr/bin/env python3
from typing import Tuple, TypeVar
from sqlalchemy import Delete, ScalarResult, Select
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio.session import AsyncSession
from db.engine import async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import class_mapper
from utils import Logs


class Base(DeclarativeBase):
    def as_dict(self):
        mapper = class_mapper(self.__class__)
        columns = [column.key for column in mapper.columns]
        return {c: getattr(self, c) for c in columns}

DBModel = TypeVar("DBModel", bound=Base)

class DatabaseConn:
    """Database connection class.
    The connection can execute, delete, and commit SQL queries.
    """
    engine: AsyncEngine = async_engine
    session: async_sessionmaker[AsyncSession]

    def __init__(self):
        self.session = async_sessionmaker(self.engine, expire_on_commit=False)

    async def rollback(self) -> None:
        async with self.session() as conn:
            await conn.rollback()

    async def execute(self, command: Select[Tuple[DBModel]]) -> ScalarResult[DBModel]|None:
        try:
            async with self.session() as conn:
                result = await conn.execute(command)
                return result.scalars()
        except Exception as e:
            Logs.log(__name__, f"{e}")

    async def delete(self, command: Delete) -> None:
        async with self.session() as conn:
            await conn.execute(command)
            await conn.commit()

    async def commit(self, model) -> None:
        async with self.session() as conn:
            conn.add(model)
            await conn.commit()
            await conn.refresh(model)

    async def merge(self, model) -> None:
        async with self.session() as conn:
            await conn.merge(model)
            await conn.commit()
            await conn.refresh(model)
