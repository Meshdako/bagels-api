from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Category(Base):
    __tablename__ = "category"

    # Audit
    createdAt = Column(DateTime, nullable=False)
    updatedAt = Column(DateTime, nullable=False)
    deletedAt = Column(DateTime, nullable=True)

    # Main columns
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    nature = Column(String(4), nullable=False)
    color = Column(String, nullable=False)

    parentCategoryId = Column(Integer, ForeignKey("category.id"), nullable=True)

    parent = relationship("Category", remote_side=[id], backref="subcategories")

    def __repr__(self):
        return f"<Category(name='{self.name}', nature='{self.nature}')>"
