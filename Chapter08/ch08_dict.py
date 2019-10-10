def isNumber(s: str) -> bool:
    '''
    어떤 문자열이 숫자(int, float)로 변환될수 있는지
    확인하는 함수
    '''
    try:
        float(s)
    except:
        return False
    return True


f = open("Chapter08\scores_list.txt", mode="r", encoding="utf-8")
score_dict: dict = {}

for line in f.readlines():
    line = line.split()
    if isNumber(line[1]):
        score_dict[line[0]] = float(line[1])

f.close()
print(score_dict)
