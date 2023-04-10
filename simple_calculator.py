# %% Homework #2

def arithmetic_ops(op):     # 연산방법(+,-,*,/,%)을 전달받고 두 수를 입력받은뒤 입력된 두 수와 연산 결과를 반환하는 함수입니다.
    num1 = int(input("input 1st number:"))      
    num2 = int(input("input 2nd number:"))
    return num1, num2, op(num1, num2)

def add(num1, num2) :      # "+"를 입력했을 때 호출되는 add 함수를 정의합니다.
    return num1+num2

def sub(num1, num2) :     # "-"를 입력했을 때 호출되는 sub 함수를 정의합니다.
    return num1-num2

while True:     # "end"를 입력하기 전까지 계산을 수행하는 반복문의 시작입니다.
    op = input("input operation:")
    if op == "end":
        break;   # 반복을 종료하고 while문을 빠져나옵니다.
    elif op == "+":
        num1, num2, ret = arithmetic_ops(add) # 정의된 함수(add) 사용하여 op에 add함수를 저장하고 arithmetic_ops 함수에서 입력된 두 수를 각각 num1, num2에, 그리고 연산결과를 ret에 저장합니다.
    elif op == "-":
        num1, num2, ret = arithmetic_ops(sub) # 정의된 함수(sub) 사용하여 op에 sub함수를 저장하고 arithmetic_ops 함수에서 입력된 두 수를 각각 num1, num2에, 그리고 연산결과를 ret에 저장합니다.
    elif op == "*":
        num1, num2, ret = arithmetic_ops(lambda num1,num2 : num1*num2) # 익명함수(lambda) 사용하여 op에 곱을 수행하는 익명함수를 부여하고, arithmetic_ops 함수에서 입력된 두 수를 각각 num1, num2에, 그리고 연산결과를 ret에 저장합니다.
    elif op == "/":
        num1, num2, ret = arithmetic_ops(lambda num1,num2 : num1/num2) # 익명함수(lambda) 사용하여 op에 나눗셈을 수행하는 익명함수를 부여하고, arithmetic_ops 함수에서 입력된 두 수를 각각 num1, num2에, 그리고 연산결과를 ret에 저장합니다.
    elif op == "%":
        num1, num2, ret = arithmetic_ops(lambda num1,num2 : num1%num2) # 익명함수(lambda) 사용하여 op에 모듈러 연산을 수행하는 익명함수를 부여하고, arithmetic_ops 함수에서 입력된 두 수를 각각 num1, num2에, 그리고 연산결과를 ret에 저장합니다.
    else:
        print("Invalid operation")
        continue    # Invalid operation이므로 연산결과를 출력하지 않고 반복문의 처음으로 돌아갑니다.

    print(f"{num1}{op}{num2} = {ret}")  # 연산 결과를 출력합니다.

    #반복문의 끝입니다.

print("Exit program")   #반복문을 빠져나왔을 때 출력하는 문장입니다. 이 이후 프로그램을 종료합니다.