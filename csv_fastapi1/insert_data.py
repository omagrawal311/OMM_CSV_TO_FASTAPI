# from fastapi import Depends
# from sqlalchemy.orm import Session
# from models import Student
# from db import *
# import pandas as pd
# import numpy as np


# def load_csv_to_db(db: Session = Depends(get_db)):
#     try:
#         path = r"C:\Users\DELL\Downloads\students_complete.csv"
#         df = pd.read_csv(path)

#         df = df.replace({np.nan: None})

#         students = []

#         for _, row in df.iterrows():
#             student = Student(
#                 student_id=row["student_id"],
#                 first_name=row["first_name"],
#                 last_name=row["last_name"],
#                 age=row["age"],
#                 major=row["major"],
#                 gpa=row["gpa"],
#                 attendance=row["attendance"],
#                 scholarship=row["scholarship"],
#                 city=row["city"]
#             )
#             students.append(student)

#         db.bulk_save_objects(students)
#         db.commit()
#         db.close()

#         return {"message": "Data inserted successfully "}

#     except Exception as e:
#         return {"error": str(e)}