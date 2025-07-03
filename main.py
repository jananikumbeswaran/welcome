from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def getmark():
    return{"hi hello welcome to github"}