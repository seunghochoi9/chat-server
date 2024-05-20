import os
from dotenv import load_dotenv
from fastapi import FastAPI
import uvicorn

from example.leap_year import LeapYear
from example.utils import myRandom
from example.grade import Grade


app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))
API_KEY = os.environ.get("API_KEY")

@app.get("/")
async def root():
    # m = BMI()
    return {"message": "Hello World 3"}


@app.get("/isLeapYear")
async def IsLeapYear():
    year = myRandom(1800, 2024)
    if LeapYear.isLeapYear(year) == True:
        return (f"{year}윤년입니다.")
    else:   
        return (f"{year}윤년이 아닙니다.")

@app.get("/grade")
async def getG():
    Grade.grade3()
    return {"message": "grade"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)