from flask import app
import numpy
from example.utils import myRandom


class Grade:

    def __init__() -> None:
        # 아래 주석된 부분을 완성합니다.
        kor = myRandom(0,100)
        eng = myRandom(0, 100)
        math = myRandom(0, 100)
        arr = [kor, eng, math]
        sum3 = sum(arr)
        avg3 = round(numpy.mean(arr)) 
        # sum = sum(kor, eng, math)
        # avg = avg(kor, eng, math)
        print(f'국어: {kor}, 영어: {eng}, 수학: {math}, 총점: {sum3}, 평균: {avg3}')
        # grade = self.getGrade()
        # passChk = self.passChk()

    def getGrade(self) -> str:
        pass

    def passChk(self) -> bool:
        pass

        