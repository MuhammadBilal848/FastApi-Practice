import uvicorn
from fastapi import FastAPI , Path
from typing import Optional

app = FastAPI()

@app.get('/')
def index(name:str = None): # here we set the query paramter to None so that it is not required
    if name == None:
        return {'Welcome': 'Stranger!!!'} 
    return {'Welcome': f'{name}'}

@app.get('/best_practice')
def best_prac(name: Optional[str] = None): # best practice is to use Optional[dtype] for handling datatypes
    if name == None:
        return {'Welcome': 'Stranger!!!'} 
    return {'Welcome': f'{name}'}

@app.get('/character')
# if we add two or more parameters, python will show error
# def char(age: Optional[int] = 19 ,  gender: Optional[str]):
# because we cant define non-default parameter after default parameter
# a workaround is that we should always define non default params before default params
# def char(  gender: Optional[str] , age: Optional[int] = 19):
# but there is another way
def char(*,age: Optional[int] =     19 ,  gender: Optional[str]):
    return {'Welcome': f'You are born in {2023 - age} and you gender is {gender}'}



student_data = {1: {
                'name':'Bilal Haneef',
                'section':'A',
                'program':'SE-Evening',
                'age':23
               }
               ,
               2: {
                'name':'Abuzar Thanvi',
                'section':'A',
                'program':'SE-Evening',
                'age':21
               },
               3: {
                'name':'Araib Irfan',
                'section':'A',
                'program':'SE-Morning',
                'age':22
               }}

@app.get('/get-student_data/{student_id}')
# we can restrict paramter such that it is only greater than 0 and we can also provide description of the params
# gt is greater than
# lt is less than
# le is less than equal to
# ge is greater than equal to
def get_stu(student_id:int = Path(description='Enter you ID provided by the university',gt=0,le = 3)):
    return student_data[student_id]


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
