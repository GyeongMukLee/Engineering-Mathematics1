while True:
    try:
        number = int(input("정수를 입력해 주세요: "))
        print("제곱의 결과는 ", number**2, "입니다.")
        break
    except:
        print("오류: 정수를 입력해주세요.")
