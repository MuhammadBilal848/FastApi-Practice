import uvicorn
from fastapi import FastAPI , Path

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Hello, World'}


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
def get_stu(student_id:int = Path(description='Enter you ID provided by the university',gt=0)):
    return student_data[student_id]


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
