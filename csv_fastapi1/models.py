from sqlalchemy import *
from db import *

class Student(Base):
    __tablename__ = "students"
    student_id = Column(String(20), primary_key=True, index=True)
    first_name = Column(String(15))
    last_name = Column(String(15))
    age = Column(Integer)
    major = Column(String(100))
    gpa = Column(Float)
    attendance = Column(Float)
    scholarship = Column(Integer)
    city = Column(String(20))
    status = Column(Enum("paid", "overdue", "pending"))