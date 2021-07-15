from typing import Optional
from fastapi import FastAPI
import uvicorn
import time

# import consumer
from consumer import data
app = FastAPI()
time.sleep(30)

print("282")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/a")
def read_root():
    return fit

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0" )