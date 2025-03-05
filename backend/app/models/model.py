from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, Float
from sqlalchemy.orm import relationship, declarative_base

# Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    telephone = Column(String(20), nullable=False)
    sex = Column(String(10), nullable=False)
    address = Column(Text, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    email = Column(String(255), unique=True, nullable=False)

# class MedicalPersonnel(Base):
#     __tablename__ = 'medical_personnel'

#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(255), nullable=False)
#     specialty = Column(String(255), nullable=False)

class MedicalRecord(Base):
    __tablename__ = 'medical_records'

    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), unique=True, nullable=False)
    creation_date = Column(Date, nullable=False)
    medical_history = Column(Text, nullable=False)
    allergies = Column(Text, nullable=False)
    blood_group = Column(String(5), nullable=False)
    on_taking_drugs = Column(Text, nullable=False)
    pulse = Column(Integer, nullable=False)
    weight = Column(Float, nullable=False)
    height = Column(Float, nullable=False)
    blood_pressure = Column(Integer, nullable=False)

    patient = relationship("Patient")

class Consultation(Base):
    __tablename__ = 'consultations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    medical_record_id = Column(Integer, ForeignKey('medical_records.id'), nullable=False)
    consultation_date = Column(Date, nullable=False)
    symptoms = Column(Text, nullable=False)
    diagnosis = Column(Text, nullable=False)

    medical_record = relationship("MedicalRecord")

class Prescription(Base):
    __tablename__ = 'prescriptions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    consultation_id = Column(Integer, ForeignKey('consultations.id'), nullable=False)
    prescription_date = Column(Date, nullable=False)

    consultation = relationship("Consultation")

class Drug(Base):
    __tablename__ = 'drugs'

    id = Column(Integer, primary_key=True, autoincrement=True)
    prescription_id = Column(Integer, ForeignKey('prescriptions.id'), nullable=False)
    drug = Column(String(255), nullable=False)
    dosage = Column(String(50), nullable=False)
    duration = Column(Integer, nullable=False)

    prescription = relationship("Prescription")

class Surgery(Base):
    __tablename__ = 'surgeries'

    id = Column(Integer, primary_key=True, autoincrement=True)
    medical_record_id = Column(Integer, ForeignKey('medical_records.id'), nullable=False)
    type_of_surgery = Column(String(255), nullable=False)
    surgery_date = Column(Date, nullable=False)

    medical_record = relationship("MedicalRecord")

class MedicalTest(Base):
    __tablename__ = 'medical_tests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    prescription_id = Column(Integer, ForeignKey('prescriptions.id'), nullable=False)
    test_type = Column(String(255), nullable=False)

    prescription = relationship("Prescription")

class Appointment(Base):
    __tablename__ = 'appointments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    appointment_date = Column(Date, nullable=False)
    motif = Column(Text, nullable=False)
    booked_by_id = Column(Integer, ForeignKey('medical_personnel.id'), nullable=True)

    patient = relationship("Patient")
    booked_by = relationship("MedicalPersonnel")




{
    "name": "John",
    "surname": "Doe",
    "date_of_birth": "1985-06-15",
    "address": "123 Main St, Cityville",
    "phone_number": "1234567890",
    "specialty": "Cardiology",
    "username": "johndoe123",
    "password_": "securepassword"
}
