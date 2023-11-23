import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.get('/home')
def home(name: str):
    return {'Welcome To Home Page': f'{name}'}

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
def get_stu(student_id:int):
    return student_data[student_id]


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
