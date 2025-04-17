from fastapi import FastAPI
from fastapi import Request

app = FastAPI()


@app.get("/get-info")
async def read_root(request : Request):
    payload = await request.json()

    first_name = payload.get("first_name")
    last_name = payload.get("last_name")
    age = payload.get("age")
    city = payload.get("city")


    # Construct the response
    response = {
        "Full Name": first_name + " " + last_name,
        "age": age,
        "city": city
    }
    # Send the response back to the client
    return response