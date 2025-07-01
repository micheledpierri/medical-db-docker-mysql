from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class PatientRecords(Base):
    __tablename__ = 'patient_records'

    Id_patient = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    date_of_birth = Column(Date, nullable=False)

    anthropometric_data = relationship("AnthropometricData", back_populates="patient")

    def __repr__(self):
        return f"<PatientRecords(Id={self.Id_patient}, Name={self.first_name} {self.last_name})>"

class AnthropometricData(Base):
    __tablename__ = 'anthropometric_data'

    Id_data = Column(Integer, primary_key=True, autoincrement=True)
    Id_patient = Column(Integer, ForeignKey('patient_records.Id_patient'), nullable=False)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)
    BMI = Column(Float, nullable=False)

    patient = relationship("PatientRecords", back_populates="anthropometric_data")

    def __repr__(self):
        return f"<AnthropometricData(Id={self.Id_data}, PatientId={self.Id_patient}, BMI={self.BMI})>"