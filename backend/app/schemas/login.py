from pydantic import BaseModel
from typing import Optional
from datetime import date


# Pydantic Schemas
class LoginStructure(BaseModel):
    """Classe de pour le login"""
    username: str
    password: str

class MedicalPersonnelBase(BaseModel):
    """classe pour MedicalPersonnel"""
    name: str
    surname: Optional[str] = None
    date_of_birth: date
    address: Optional[str] = None
    phone_number: str
    specialty: str
    username: str

class MedicalPersonnelCreate(MedicalPersonnelBase):
    password_: str

class MedicalPersonnelResponse(MedicalPersonnelBase):
    id: int

    class Config:
        from_attributes = True


class PasswordBase(BaseModel):
    password_: str

class PasswordCreate(PasswordBase):
    pass

class PasswordResponse(PasswordBase):
    id: int

    class Config:
        from_attributes = True

