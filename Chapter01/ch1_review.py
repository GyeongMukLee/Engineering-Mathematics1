import math


def box_surface(a, b, c):
    '''
    문제 6. 변의 길이가 각각 a,b,c인
    직각육면체의 표면적을 계산해주는 함수
    '''
    return 2*(a*b+b*c+a*c)


def even_test(n):
    '''
    문제 7. 주어진 자연수 n이 짝수면 True, 아니면 False를 리턴해주는 함수
    '''
    if n % 2 == 0:
        return True
    else:
        return False


def circle_area(r):
    '''
    문제 8. 반지름이 r인 원의 넓이를 구하는 함수
    '''
    return math.pi*(r**2)


def triangle_area(a, b, c):
    '''
    문제 9. 변의 길이가 각각 a,b,c인
    삼각형의 면적 A를 계산하는 함수
    '''
    p = (a+b+c)/2
    return math.sqrt(p*(p-a)*(p-b)*(p-c))


def eq_triangle_area(a):
    '''
    문제 10. 정삼각형의 넓이를 구하는 함수
    '''
    return (math.sqrt(3)/4)*(a**2)


print(triangle_area(1, 1, 1))
print(eq_triangle_area(1))
