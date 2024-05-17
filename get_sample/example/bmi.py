from utils import Member


class BMI():
    def __init__(self) -> None:
        '''utils.py / Members(), myRandom() 를 이용하여 BMI 지수를 구하는 계산기를 작성합니다.'''
        
    def getBMI(self) -> str:

        this = Member()
        this.name = '홍길동'
        this.height = 170.5    
        this.weight = 80.5
        result = round(this.weight / ((this.height/100) ** 2), 2) 
        if result < 18.5:
            return '저체중'
        elif 18.5 <= result < 23:
            return '정상'
        elif 23 <= result < 25:
            return '과체중'
        elif 25 <= result < 30:
            return '비만'
        else:
            return '고도비만'