import uvicorn
from fastapi import FastAPI , Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# we will use post method now, so first we have to create base model (means we have to define what we want to
# take from user that we want to post)
# for that we have to define class

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
        print('printing age param')
        print(age)
        print('printing student_data[student_id]age')
        print(student_data[student_id],type(student_data[student_id]))
        print(student_data[student_id]['age'])
        print(age == student_data[student_id]['age'])
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
    return student_data


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)






