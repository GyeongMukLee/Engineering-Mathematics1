def geometric_mean(a, b):
    """
    두 숫자의 기하평균을 구하는 함수
    """
    return (a*b)**(1/2)


def distance(a, b):
    """
    두 점 사이의 거리를 구하는 함수
    """
    return abs(b-a)


def pyramid_value(A, h):
    """
    바닥 면적이 A이고 높이가 h인 피라미드의 부피를 구하는 함수
    """
    return (1/3)*A*h


def second_to_day(sec):
    """
    초 단위의 시간을 받아서 일 단위의 값을 리턴하는 함수
    """
    return sec//(24*60*60)
