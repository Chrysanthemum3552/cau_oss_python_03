import figure # 아래 코드에서 " figure.* " 형태로 figure의 메서드를 사용하고 있으므로 from~import가 아닌 import를 이용하여 figure 모듈을 가져옵니다.

myline = figure.line(10)

square = figure.area_square(myline.get_length())
print(square)

myline.set_length(20)
regular_triangle = figure.area_regular_triangle(myline.get_length())
print(regular_triangle)

myline.set_length(30)
circle = figure.area_circle(myline.get_length())
print(circle)