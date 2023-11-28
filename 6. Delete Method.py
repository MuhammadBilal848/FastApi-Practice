import uvicorn
from fastapi import FastAPI , Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


student_data = {1: {
                'name':'Bilal Haneef',
                'section':'A',
                'program':'SE-Evening',
                'age':23
               }}

class Student(BaseModel):
    name : str
    section : str
    program : str
    age : int

# added default None because user may want to edit just one variable.
class UpdateStudent(BaseModel):
    name : Optional[str] = None
    section : Optional[str] = None
    program : Optional[str] = None
    age : Optional[int] = None



@app.get('/')
def index(name:str = None): # here we set the query paramter to None so that it is not required
    if name == None:
        return {'Welcome': 'Stranger!!!'} 
    return {'Welcome': f'{name}'}

# @app.get('/get-student_data/{student_id}')
# def get_stu(student_id:int):
#     return student_data[student_id]

@app.get('/get-info/{student_id}')
def info(student_id:int ,age:int):
    if student_id in student_data:
        if age == student_data[student_id]['age']:
            return student_data[student_id]
        return {'Message':'You entered wrong age information!'}
    else:
        return {'Error':'You have entered wrong id'}

@app.post('/post-create_student/{student_id}')
def create_student(student_id : int , student : Student ): 
    # here student : Student , 'student' is a parameter and 'Student' is a basemodel class that we defined,
    # it is kinda key value thing, now when this endpoint is called, it will ask user to fill the details
    # defined in the Student class.
    if student_id in student_data:
        return {'Error':'Student alreay exist in the records'}
    student = student.dict() # this will convert the student class variable object into dict
    student_data[student_id] = student
    return student_data[student_id]

@app.put('/put-edit_info/{student_id}')
def edit_info(student_id : int , updatestudent : UpdateStudent):
    if student_id not in student_data:
        return {'Error':'Student does not exist in the records'}    
    
    if updatestudent.name != None:
        student_data[student_id]['name'] = updatestudent.name
    if updatestudent.section != None:
        student_data[student_id]['section'] = updatestudent.section
    if updatestudent.program != None:
        student_data[student_id]['program'] = updatestudent.program
    if updatestudent.age != None:
        student_data[student_id]['age'] = updatestudent.age
    return student_data[student_id]


# here we will create a delete method that deletes an item from dictionary
@app.delete('/delete-student_del/{student_id}')
def student_del(student_id : int):
    if student_id not in student_data:
        return {'Error':'Student does not exist in the records'}    
    del student_data[student_id]
    return {'Success':'Student is deleted successfully.'}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)






