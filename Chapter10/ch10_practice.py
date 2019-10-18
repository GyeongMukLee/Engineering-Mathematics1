def infoFileToDict(dir: str) -> list:
    """
    (학생 정보 파일만 있는)디렉터리를 입력하면
    학생 정보 파일을 리스트로 변환하는 함수
    """


def printFirstStudent(studentDict: list) -> None:
    """
    첫 번째 학생의 신상정보를 

    "제 이름은 (이름)이고, 나이는 (나이)살 입니다."

    형태로 출력하는 함수
    """
    print("제 이름은", studentDict[0]["Name"], "이고, 나이는",
          2020-studentDict[0]["Date of Birth"][0], "살 입니다.")
    return None


def departmentStudentList(studentDict: list, department: str) -> list:
    """
    전공을 인자로 입력하면 해당 전공을 가진 학생을 리스트를 리턴하는 함수
    """
    return_list: list = []

    for i in studentDict:
        if (i["Department"] == department):
            return_list.append(i["Name"])

    return return_list
