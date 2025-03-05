from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.database import Base

class MedicalPersonnel(Base):
    __tablename__ = 'medical_personnel'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=True)
    date_of_birth = Column(Date)
    address = Column(String(255), nullable=True)
    phone_number = Column(String(20), nullable=False)  # Changed from Integer to String
    specialty = Column(String(255), nullable=False)
    username = Column(String(255), unique=True, index=True)

    compte_securities = relationship(
        "Password", back_populates="user_a_compte", uselist=False, cascade="all, delete-orphan"
    )
