def strToDate(date: str) -> tuple:
    """
    YY.MM.DD형태의 문자열이 들어올 경우
    (YYYY, MM, DD)형태의 튜플을 리턴하는 함수
    """
    year, month, day = map(int, date.split("."))

    if(year >= 19):
        year += 1900
    else:
        year += 2000

    return (year, month, day)


def studentFiletoList(filename: str) -> list:
    """
    파일로 주어진 학생의 개인정보를
    리스트로 리턴하는 함수
    """
    import string
    std_data = list()
    fp = open(filename, mode="r", encoding="utf-8")

    for li in fp.readlines():
        if (li[0] == "#") or (li in string.whitespace):
            continue
        else:
            item, value = li.split(":")
            item = item.strip()
            value = value.strip()
            if item == "Date of Birth":
                value = strToDate(value)
            std_data.append((item, value))

    return std_data


def studentListFindDepartment(li: list) -> str:
    """
    studentFiletoList()함수로 만들어진 리스트에서
    학과를 찾아 리턴하는 함수
    """
    for i in li:
        if i[0] == "Department":
            return i[1]


Byun_Sato = studentFiletoList("Chapter09/Students_Records/Byun_Sato.txt")
print(Byun_Sato)

print(studentListFindDepartment(Byun_Sato))
