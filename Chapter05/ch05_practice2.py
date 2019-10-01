def BMI(height: float, weight: float):
    '''
    BMI를 계산하는 함수
    '''
    try:
        return weight/(height**2)
    except ZeroDivisionError as e:
        print("오류: ", e)
    except TypeError as e:
        print(e)


def judgeBMI(BMI: float):
    '''
    입력된 BMI를 이용해 체중이 어느 정도인지 판단하는 함수
    '''
    try:
        if myBMI >= 25:
            return "비만"
        elif myBMI >= 23:
            return "과체중"
        elif myBMI >= 18.5:
            return "정상"
        else:
            return "저체중"
    except TypeError as e:
        print("오류: ", e)


myBMI = BMI(float(input("키(m)를 입력해주세요: ")),
            float(input("체중(kg)를 입력해 주세요: ")))

print(judgeBMI(myBMI), "입니다.")
