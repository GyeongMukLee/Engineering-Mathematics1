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


def scoreFileToDict(filename: str) -> dict:
    f = open(filename, mode="r", encoding="utf-8")
    score_dict: dict = {}

    for line in f.readlines():
        line = line.split()
        if isNumber(line[1]):
            score_dict[float(line[1])] = line[0]

    f.close()
    return score_dict


def scoreDictSort(scoredict: dict) -> list:
    '''
    scoreFileToDict()함수를 통해 만든 dict를
    점수 순서대로 정렬하는 함수

    [[1등선수, 점수], [2등선수, 점수], ...]
    '''
    return_list: list = []
    keys = list(scoredict.keys())
    keys.sort()
    keys.reverse()

    for i in keys:
        return_list.append([scoredict[i], i])

    return return_list


def scoreRankPrint(scoredict: dict, last: int) -> None:
    '''
    scoreFileToDict()함수를 통해 만든 dict를
    점수 순서대로 프린트하는 함수

    last 인수에 자연수를 입력하면 그 등수만큼만 출력함
    '''
    j = 1
    for i in scoreDictSort(scoredict):
        if j > last:
            return None
        print("%-2d등 %-10s %2.2f" % (j, i[0], i[1]))
        j += 1

    return None


scoredict = scoreFileToDict("Chapter08\scores_list.txt")
print(scoredict)
print(scoreDictSort(scoredict))
scoreRankPrint(scoredict)
scoreRankPrint(scoredict, 3)
