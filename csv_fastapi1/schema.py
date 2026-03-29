from pydantic import BaseModel,Field
from typing import Annotated,Literal

class Student(BaseModel):

    student_id:Annotated[str,Field(...,examples=['STU_1000'])]
    first_name:Annotated[str,Field(...,description="Enter your first name only",max_length=15)]
    last_name:Annotated[str,Field(...,description="Enter your last name",max_length=15)]
    age:Annotated[int,Field(...,description="Enter your age",gt=0,lt=120)]
    major:Annotated[str,Field(...,description="Enter your subject")]
    gpa:Annotated[float,Field(...,description="Enter your gpa")]
    attendance:Annotated[float,Field(...,description="Enter your attendance percentage",examples="0.89")]
    scholarship:Annotated[int,Field(...,description="Enter your scholarship amt if you get oherwise enter 0")]
    city:Annotated[str,Field(...,description="Enter your city",max_length=20)]
    status:Annotated[Literal["paid","overdue","pending"],Field(...,description="Enter your fees status")]


    




