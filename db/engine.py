#!/usr/bin/env python3
from utils.env import Env
from sqlalchemy import event
from sqlalchemy.ext.asyncio import create_async_engine
url = f"postgresql+asyncpg://{Env.DB_USERNAME}:{Env.DB_PASSWORD}@{Env.DB_HOST}/{Env.DB_NAME}"
async_engine = create_async_engine(url)

@event.listens_for(async_engine.sync_engine, "connect")
def do_connect(dbapi_connection, connection_record):
    # disable aiosqlite's emitting of the BEGIN statement entirely.
    # also stops it from emitting COMMIT before any DDL.
    dbapi_connection.isolation_level = None

@event.listens_for(async_engine.sync_engine, "begin")
def do_begin(conn):
    # emit our own BEGIN
    conn.exec_driver_sql("BEGIN")
