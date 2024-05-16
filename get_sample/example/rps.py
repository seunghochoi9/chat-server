


from example.utils import myRandom


class RPS:

    def my3(): 
        if myRandom(1,4) == 1:
            return "가위"
        elif myRandom(1,4) == 2:
            return "바위"
        else:    
            return "보"
