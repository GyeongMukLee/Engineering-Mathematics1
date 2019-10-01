def shoppingListParsing(file: str) -> list:
    """
    상품 개수 가격

    형태로 작성된 파일을 리스트로 가져오는 함수
    """
    try:
        fp = open(file, "r")
        shoppingList = fp.read().split("\n")
        fp.close()

        for i in range(len(shoppingList)):
            shoppingList[i] = shoppingList[i].split()
            shoppingList[i][1] = int(shoppingList[i][1])
            shoppingList[i][2] = float(shoppingList[i][2])

    except TypeError as Te:
        print(Te)

    except ValueError as Ve:
        print(Ve)

    except FileNotFoundError as FNe:
        print(FNe)
        exit()

    return shoppingList


def shoppingListAmount(shoplist: list) -> float:
    """
    shoppingListParsing()함수로 파싱된 리스트를 입력받아
    총 가격을 구하는 함수
    """
    sum: int = 0

    for i in range(len(shoplist)):
        sum += shoplist[i][1]*shoplist[i][2]

    return sum


def shoppingListAdd(shoplist: list, item: str, count: int, price: float) -> None:
    """
    shoppingListParsing()함수로 파싱된 리스트와 상품, 개수, 가격을 받아
    쇼핑리스트에 추가하는 함수
    """
    shoplist.append([item, count, price])
    return None


def shoppingListAdd(shoplist: list, addlist: list):
    """
    shoppingListParsing()함수로 파싱된 리스트와 [상품, 개수, 가격]을 받아
    쇼핑리스트에 추가하는 함수
    """
    shoplist.append(addlist)
    return None
