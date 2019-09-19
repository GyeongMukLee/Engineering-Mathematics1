def sumIfEndswith3(k: int, m: int):
    '''
    두 개의 자연수 k,m이 주어졌을 때
    만약 m이 3의 배수이거나 3으로 끝나는 숫자일 경우
    k와 m을 더하고, 아닌 경우에는 k를 return
    '''
    if m % 3 == 0 or str(m).endswith("3"):
        return k+m
    else:
        return k


def sumIf3(k: int, m: int):
    '''
    두 개의 정수 k,m이 주어졌을 때
    만약 m이 3의 배수이거나 3을 포함하는 숫자일 경우
    k와 m을 더하고, 아닌 경우에는 k를 return
    '''
    if m % 3 == 0 or ("3" in str(m)):
        return k+m
    else:
        return k


def divide(num: int, divisor: int):
    '''
    num을 devisor로 나누었을 때 몫을 반환하는 함수
    '''
    returnVal = 0

    while num >= divisor:
        num -= divisor
        returnVal += 1

    return returnVal


def greatCommonFactor(a: int, b: int):
    '''
    유클리드 호제법을 이용하여
    a와 b의 최대공약수를 구하는 함수

    - 유클리드 호제법
    1. 작은 수로 큰 수로 나눈다. 만약 나누어 떨어지면 최대공약수는 작은 수
    2. 아니라면 작은 수를 나머지로 나눈다.
    '''
    if a < b:
        a, b = b, a

    rest = a % b

    if rest == 0:
        return b
    else:
        greatCommonFactor(b, rest)


print(greatCommonFactor(15, 6))


def sumOfThree(n: int):
    '''
    1부터 n까지의 자연수 중에서
    3의 배수이거나 3을 포함하는 자연수의 합을
    구하는 함수
    '''
    returnVal = 0

    for i in range(1, n+1):
        if i % 3 == 0 or ("3" in str(i)):
            returnVal += i

    return returnVal
