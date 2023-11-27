import uvicorn
from fastapi import FastAPI , Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index(name:str = None): # here we set the query paramter to None so that it is not required
    if name == None:
        return {'Welcome': 'Stranger!!!'} 
    return {'Welcome': f'{name}'}

@app.get('/get-info/{student_id}')
def info(*, student_id:int = Path(ge = 0,le = 3),age:int):
    if age == student_data[student_id]['age']:
        return student_data[student_id]
    return {'Message':'You entered wrong information!'}


# we will use post method now, so first we have to create base model (means we have to define what we want to
# take from user that we want to post)
# for that we have to define class

class Student(BaseModel):
    name : str
    section : str
    program : str
    age : int

student_data = {1: {
                'name':'Bilal Haneef',
                'section':'A',
                'program':'SE-Evening',
                'age':23
               }}

# @app.post('/post/')



# student_data = {1: {
#                 'name':'Bilal Haneef',
#                 'section':'A',
#                 'program':'SE-Evening',
#                 'age':23
#                }
#                ,
#                2: {
#                 'name':'Abuzar Thanvi',
#                 'section':'A',
#                 'program':'SE-Evening',
#                 'age':21
#                },
#                3: {
#                 'name':'Araib Irfan',
#                 'section':'A',
#                 'program':'SE-Morning',
#                 'age':22
#                }}

# here we combined the qurery and the path parameter




if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
