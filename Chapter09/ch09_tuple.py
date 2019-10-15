# 튜플: 변하지 않는 시퀀스 자료형
week = ("Mon", "Tue", "Wed", "Sat", "Sun")

# 괄호를 생략해도 튜플이 된다.
istuple = 10, 20, 30, 40, 50
print(type(istuple), istuple)


# 인덱스를 지정할 수 있다.
print(week[1], week[-1], week[::2])


def f(x) -> tuple:
    '함수에서 여러 개의 값을 리턴하고 싶을때 튜플을 사용한다'
    return x**2, x**3


# 튜플은 값을 변경할 수 없다.
HW = ("Hello", "World", "!")
try:
    HW[0] = "Hell"
except TypeError as e:
    print(e)
    pass


# 길이가 1인 튜플 만드는 방법
single = (1,)
print(type(single), single)

# 튜플에 리스트가 포함된 경우
listInTuple = ([1, 2, 3, 4], 10)
listInTuple[0] = [1, 2, 3, 4, 5]  # 오류
listInTuple[0].append(5)

# 튜플의 메소드
tuplemethod = ("b", "b", "c", "c", "c")
print(tuplemethod.count("b"))
print(tuplemethod.index("c"))
