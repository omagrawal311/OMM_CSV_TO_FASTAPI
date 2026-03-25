from fastapi import FastAPI,HTTPException,Path,Query
import pandas as pd
import numpy as np


app=FastAPI()

@app.get("/")
def home():
    return {"Message":"Hello world"}

def load_data():
    path=r"C:\Users\DELL\Downloads\students_complete.csv"
    df=pd.read_csv(path)
    df = df.replace({np.nan: None})
    data=df.to_dict(orient="records")
    return data

@app.get("/viewstudents")
def view():
    data=load_data()
    return data
      
@app.get("/students/{student_id}")
def view_student(student_id: str=Path(...,description="Please Provide valid Student ID",example="STU_1000")):
    data = load_data()

    for student in data:
        if student["student_id"] == student_id:
            return student

    raise HTTPException(status_code=404, detail="student not found")

@app.get("/sort_students")
def sort_student(sort_by:str=Query(...,description="You can sort by [age]")):
    valid_fields=['age']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f"Invalid feilds Please select from {valid_fields}")
    data=load_data()
    sorted_data = sorted(data, key=lambda x: x.get(sort_by, ""))
    return sorted_data

