from database import Base 
from sqlalchemy import Column, Integer, String, Boolean, Enum
import enum

class CategoryEnum(enum.Enum):
    technology = "technology"
    finance = "finance"
    music = "music"

class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    is_published = Column(Boolean, default=False)
    category = Column(Enum(CategoryEnum), nullable=False)
