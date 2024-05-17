from flask import app
import numpy
from example.utils import myRandom


class Grade:

    def __init__() -> None:
        # 아래 주석된 부분을 완성합니다.
        pass


    def grade3() -> str:
        kor = myRandom(0,100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        arr = [kor, eng, math]
        sum3 = sum(arr)
        avg3 = round(numpy.mean(arr)) 
        print(f'국어: {kor}, 영어: {eng}, 수학: {math}, 총점: {sum3}, 평균: {avg3}')
        getggg = getggg(avg3)
        passChk = passChk(avg3)
        print(f'평균: {avg3}, 학점: {getggg}, {passChk}')
    
    

def getggg(avg3) -> str:
    if avg3 >= 90:
        return 'A'
    elif avg3 >= 80:
        return 'B'
    elif avg3 >= 70:
        return 'C'
    elif avg3 >= 60:
        return 'D'
    else:
        return 'F'

def passChk(avg3) -> str:
    if avg3 >= 60:
        return "합격"
    else:
        return "불합격"

        