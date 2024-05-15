#!/usr/bin/env python3
from db.base import DatabaseConn

class BaseTable:
    def __init__(self):
        self._conn: DatabaseConn = DatabaseConn()
