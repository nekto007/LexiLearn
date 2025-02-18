from datetime import datetime
from typing import Optional, List
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs

from vocabulary_builder.constants import DownloadStatus, WordLevel


class Base(DeclarativeBase, AsyncAttrs):
    __tablename__ = 'words'

    id = Column(Integer, primary_key=True, autoincrement=True)
    english_word = Column(String, unique=True, index=True, nullable=False)
    russian_word = Column(String, nullable=True)
    listening_file = Column(String, nullable=True)
    is_brown = Column(Boolean, default=False)
    word_level = Column(Enum(WordLevel), nullable=True)
    download_status = Column(Enum(DownloadStatus), default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


    books = relationship("BookWord", back_populates="words")

class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, unique=True)
    author = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    words = relationship("BookWord", back_populates="book")


class BookWord(Base):
    __tablename__ = 'book_words'

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    word_id = Column(Integer, ForeignKey('words.id'), nullable=False)
    frequency = Column(Integer, nullable=False)

    book = relationship('Book', back_populates='words')
    word = relationship('Word', back_populates='books')
