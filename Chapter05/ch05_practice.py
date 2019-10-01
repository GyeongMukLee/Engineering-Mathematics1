def divideBy100(number):
    '''
    [문제1]
    100을 입력한 값으로 나누는 함수를 작성하라.

    1. 0이 아닌 숫자가 입력될 경우 100을 그 숫자로 나눔
    2. 0이 입력되면 0이 아닌 숫자를 입력하라는 문구를 출력
    3. 숫자가 아닌 값이 입력되면 숫자를 입력하라는 문구를 출력
    '''
    try:
        return 100/number
    except TypeError:
        print("숫자를 입력해주세요.")
    except ZeroDivisionError:
        print("0이 아닌 다른 숫자를 입력해주세요.")


def divideAbyB(a, b):
    '''
    [문제2]
    두 개의 숫자 a, b를 입력받아 a/b를 계산하는 함수

    1. 0이 아닌 숫자가 입력될 경우 100을 그 숫자로 나눔
    2. 0이 입력되면 0이 아닌 숫자를 입력하라는 문구를 출력
    3. 숫자가 아닌 값이 입력되면 숫자를 입력하라는 문구를 출력

    '''
    try:
        return a/b
    except TypeError as e:
        print("숫자를 입력하세요.")
        return e
    except ZeroDivisionError as e:
        print("0으로 나눌 수 없습니다.")
        return e


print(divideAbyB(5, "0"))
