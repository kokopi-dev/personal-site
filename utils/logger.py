#!/usr/bin/env python3
from enum import Enum
import logging
from utils.env import Env
import sys

class LogLevel(Enum):
    info = logging.INFO
    warning = logging.WARNING
    error = logging.ERROR

class LogsBase:
    _loggers: dict[str,logging.Logger]

    def __init__(self):
        if Env.ENV == "dev":
            self._handler = logging.StreamHandler(sys.stdout)
        else:
            self._handler = logging.FileHandler("app.log")

        formatter = logging.Formatter('%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s')
        self._handler.setFormatter(formatter)
        self._loggers = {}

    def log(self, name: str, message: str|Exception, level: LogLevel = LogLevel.info) -> None:
        logger: logging.Logger|None = self._loggers.get(name)
        if not logger:
            _log = logging.getLogger(name)
            _log.addHandler(self._handler)
            _log.setLevel(logging.DEBUG)
            self._loggers[name] = _log
            logger = _log
        logger.log(level.value, message, stacklevel=2)

Logs = LogsBase()
