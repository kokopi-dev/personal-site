#!/usr/bin/env python3
from datetime import datetime

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
import uuid

from db.base import Base

blog_tags = Table(
    "kokopi_dev_blog_tags",
    Base.metadata,
    Column("kokopi_dev_blog_id", UUID, ForeignKey("kokopi_dev_blogs.id", ondelete="CASCADE")),
    Column("kokopi_dev_tag_id", UUID, ForeignKey("kokopi_dev_tags.id", ondelete="CASCADE"))
)

class BlogCategory(Base):
    __tablename__ = "kokopi_dev_categories"
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(length=32), unique=True)
    blogs: Mapped[list["Blog"]] = relationship(
      "Blog",
      back_populates="category"
  )

class BlogTag(Base):
    __tablename__ = "kokopi_dev_tags"
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(length=32), unique=True)
    blogs: Mapped[list["Blog"]] = relationship(
       "Blog",
       secondary=blog_tags,
       back_populates="tags",
       passive_deletes=True
   )

class Blog(Base):
    __tablename__ = "kokopi_dev_blogs"
    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    filename: Mapped[str] = mapped_column(String(length=120), default="")
    title: Mapped[str] = mapped_column(String(length=160), unique=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=func.now())
    author: Mapped[str] = mapped_column(String(length=50), nullable=True)
    category_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("kokopi_dev_categories.id"))
    category: Mapped["BlogCategory"] = relationship("BlogCategory", back_populates="blogs", cascade="all, delete")
    tags: Mapped[list["BlogTag"]] = relationship(
       "BlogTag",
       secondary=blog_tags,
       back_populates="blogs",
       cascade="all, delete"
   )

