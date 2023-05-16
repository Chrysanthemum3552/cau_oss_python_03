import math  # sqrt와 pi를 사용할 것이므로 math모듈을 import합니다.

class line: 
    def __init__(self, length=0): # 입력이 없으면 0의 값을 그 외에는 입력한 값을 매개변수 length에 저장합니다.    
        self.__length=length # __init__을 이용하여 외부에서 접근할 수 없는 변수 __length을 매개변수 length 값으로 초기화합니다.

    def set_length(self, n):
        self.__length=n # __length의 값을 설정하는 메소드입니다.
    
    def get_length(self):
        return self.__length # __length의 값을 반환해주는 메소드입니다.
    

def area_square(length): # 정사각형 한 변의 길이를 입력받습니다.
    return length**2 # 정사각형의 넓이를 구하여 값을 반환합니다.

def area_circle(length): # 원의 반지름 값을 입력받습니다.
    return (length**2)*math.pi # 원의 넓이를 구하여 값을 반환합니다.

def area_regular_triangle(length): # 정삼각형 한 변의 길이를 입력받습니다.
    return (math.sqrt(3)/4)*(length**2) # 정삼각형의 넓이를 구하여 값을 반환합니다.