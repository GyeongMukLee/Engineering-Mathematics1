try:
    number = int(input("정수를 입력해주세요: "))
    print("5/(x-4) = ", 5/(number-4))
except ValueError:
    print("정수를 입력하세요.")
except ZeroDivisionError:
    print("4가 아닌 다른수를 입력하세요.")
