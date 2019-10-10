def scoreFileToList(filename: str) -> list:
    fp = open(filename, mode="r")
    scoreList: list = list()
    for line in fp.readlines():
        score = line.split()[1]
        if not score.isalpha():
            scoreList.append(float(score))

    return scoreList


def ranking(li: list, rank: int) -> float:
    try:
        li.sort()
        li.reverse()
        return li[rank-1]
    except IndexError:
        return -1


print(ranking(scoreFileToList("Chapter07\scores_list.txt"), 1))


# ======================================================= #

li: list = [1, 2, [3, 4], [[5, 6, 7], 8]]
print(li[1], li[2], li[2][0], li[3][0][2])

# ======================================================= #

animals = ["dog", "cat", "pig"]
print(animals)

animals.append("coq")
print(animals)

animals.append(["eagle", "bear"])
print(animals)
# [eagle, bear] 자체가 animals 리스트의 원소로 들어가게 된다.

animals.remove(["eagle", "bear"])
print(animals)

animals.extend(["eagle", "bear"])
print(animals)

animals[1]="cow"
print(animals)

print(animals[1:4])

animals[1:4]=["tiger","lion","rabbit"]
print(animals)

animals[1:2]=[]
print(animals)

