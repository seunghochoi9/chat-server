from fastapi import FastAPI
import uvicorn

from example.rps import RPS
from example.leap_year import LeapYear
from example.utils import myRandom
from example.grade import Grade


app = FastAPI()


@app.get("/")
async def root():
    # m = BMI()
    return {"message": "Hello World 3"}

@app.get("/rps")
async def rps():
    return RPS.my3()

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