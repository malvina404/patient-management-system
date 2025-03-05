
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Password(Base):
    __tablename__ = 'passwords'

    id = Column(Integer, ForeignKey('medical_personnel.id'), primary_key=True)  # Fixed table reference
    password_ = Column(String(254), index=True)

    user_a_compte = relationship("MedicalPersonnel", back_populates="compte_securities")
