string = "Python"
for i in string:
    print(i)


def findDog(sentence: str):
    '''
    평문을 하나 받아서 그 문장 안에
    dog가 포함되어있으면 true를 반환하는 함수
    '''
    sentence.lower()
    if "dog" in sentence:
        return True
    else:
        return False


print(findDog("adklfjadlfkdogdlfkajdsfklj"))


def sumOfMultipleOfThreeAndContainThree(n: int):
    '''
    자연수 n을 받아서, 1부터 n까지의 자연수 중
    3의 배수이거나 3이 포함된 수를 합하는 함수
    '''
    sum = 0
    for i in range(1, n+1):
        if (i % 3 == 0) or ("3" in str(i)):
            sum += i

    return sum


print(sumOfMultipleOfThreeAndContainThree(3))


stringExample = "Voluptatem rerum at hic animi laborum error non. \
                Ut in officia eligendi officia reiciendis dolor. \
                Enim nemo quasi explicabo id delectus ad aliquam praesentium. \
                Aut est dolor quis assumenda sapiente qui aliquam adipisci aliquam."


def lowerAtoUpper(sentence: str):
    '''
    문장의 모든 소문자a를 대문자A로 변경하여 반환하는 함수
    '''
    newSentace = sentence

    for i in range(len(sentence)):
        if sentence[i] == "a":
            newSentence[i] = "A"

    return newSentace


def countA(sentence: str):
    '''
    문장의 모든 a를 세는 함수
    '''
    count = 0
    for i in sentence:
        if i == "a":
            count += 1

    return count
