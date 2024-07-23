import uvicorn
from fastapi import FastAPI
from fastapi import File, UploadFile
from testing import prediction
import io
import numpy as np
import cv2

app = FastAPI()

@app.get('/')
def index():
    return {'message': 'Welome to the API'} 


@app.post("/post-image_inference/")
async def image_inference(file: UploadFile = File(...)):
    contents = await file.read()
    image = io.BytesIO(contents)
    np_img = np.frombuffer(image.read(), np.uint8)
    cv_img = cv2.imdecode(np_img, cv2.IMREAD_COLOR)
    
    return prediction(cv_img)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
