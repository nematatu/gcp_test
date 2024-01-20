from fastapi import FastAPI

app=FastAPI()

@app.get("/hello")
def hello():
    return {'message':'Hello!'}

@app.get("/world")
def world():
    return {'message':'world!'}