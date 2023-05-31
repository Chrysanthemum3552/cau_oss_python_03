import math  # pi를 사용할 것이므로 math모듈을 import합니다.

class line: 
    def __init__(self, width=0, height=0): # 입력이 없으면 0의 값을 그 외에는 입력한 값을 매개변수 width, height에 저장합니다.    
        self.__width=width # 생성자를 이용하여 외부에서 접근할 수 없는 변수 __width을 매개변수 width 값으로 초기화합니다.
        self.__height=height # 생성자를 이용하여 외부에서 접근할 수 없는 변수 __height을 매개변수 height 값으로 초기화합니다.

    def set_length(self, width, height): # 외부에서 직접 변수를 수정할 수 없어서 이를 수정가능하게 하는 함수입니다.
        self.__width=width  # 매개변수 width가 받은 값을 __width에 저장합니다.
        self.__height=height # 매개변수 height가 받은 값을 __height에 저장합니다.
    
    def get_length(self):
        return self.__width, self.__height # __length의 값을 반환해주는 메소드입니다.
    

def area_rectangle(width, height): # 직사각형의 너비와 높이를 받아 각각 매개변수 width, length에 저장합니다.
    if width<=0 or height<=0: raise ValueError # 만약 width나 height값이 0이하면 ValueError을 발생시킵니다.
    return width*height # 직사각형의 넓이를 구하여 이 값을 반환합니다.

def area_ellipse(width, height): # 타원의 장반지름과 단반지름을 받아 각각 매개변수 width, length에 저장합니다.
    if width<=0 or height<=0: raise ValueError # 만약 width나 height값이 0이하면 ValueError을 발생시킵니다.
    return width*height*math.pi # 타원의 넓이를 구하여 값을 반환합니다.

def area_right_triangle(width, height): # 직각삼각형의 밑변과 높이를 받아 각각 매개변수 width, height에 저장합니다.
    if width<=0 or height<=0: raise ValueError # 만약 width나 height값이 0이하면 ValueError을 발생시킵니다.
    return (width*height)/2 # 직각삼각형의 넓이를 구하여 값을 반환합니다.