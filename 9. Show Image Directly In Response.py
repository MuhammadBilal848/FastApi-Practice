import io
import cv2
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import FastAPI, File, UploadFile 
from fastapi.responses import StreamingResponse

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/post-uploadfile/")
async def image_upload(file: UploadFile = File(...)):
    content = await file.read()
    with open(file.filename, "wb") as f:
        f.write(content)


    image = cv2.imread(file.filename)
    _, img_encoded = cv2.imencode('.jpg', image)
    img_bytes = io.BytesIO(img_encoded) 

    return StreamingResponse(img_bytes, media_type="image/jpeg")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)




