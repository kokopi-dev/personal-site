#!/usr/bin/env python3
"""Models for accessing private db
"""
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
import uuid

from db.base import Base

class PersonalBlogMetaModel(Base):
    __tablename__ = "personal_blog_metas"
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    url: Mapped[str] = mapped_column(String(), default="")
    image_url: Mapped[str] = mapped_column(String(), default="")
    title: Mapped[str] = mapped_column(String(), default="")
    description: Mapped[str] = mapped_column(String(), default="")
