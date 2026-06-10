from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from database import Base

class Account(Base):
    __tablename__ = "account"

    # Audit columns
    createdAt = Column(DateTime, nullable=False)
    updatedAt = Column(DateTime, nullable=False)
    deletedAt = Column(DateTime, nullable=True) #Soft delete

    # Main columns
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    beginningBalance = Column(Float, nullable=False)
    repaymentDate = Column(Integer, nullable=True)
    hidden = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"<Account(name='{self.name}', balance={self.beginningBalance})>"

