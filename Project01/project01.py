def fibo(n: int) -> int:
    """
    자연수 n을 입력받아 n 번째 피보나치 수를 리턴하는 함수 fibo(n)를 구현하라.

    참고) fibo(1) = 1, fibo(2) = 1, fibo(n) = fibo(n-1) + fibo(n-2)이다.

    test) fibo(5) = 5, fibo(10) = 55
    """
    if n == 1 or n == 2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)


def shopping_total_sum(shopping_file: str) -> float:
    """
    쇼핑리스트(첨부파일)을 입력받아, 총 가격을 리턴하는 함수 shopping_total_sum(shopping_file)를 구현하라.
    단, 이 함수는 아래의 조건을 만족시킨다.

    (1) 함수가 실행된 후, 구매가능한 물품과 가격을 출력한다.
        이후 구매할 물품과 수량을 입력하면, 선택한 물품에 대한 총 가격을 리턴해준다. 

    (2) 발생할 수 있는 오류에 대한 예외 처리를 한다. 

    test) shopping_total_sum('shopping_list.txt') 을 실행 후,
       tomato : 1, cola : 2를 입력하면,  5000원을 리턴해준다.
    """
    try:
        file = open(shopping_file, mode="r", encoding="utf-8")
        shopping_list = file.read().split("\n")
        shopping_dict: dict = {}     # 제품명:가격
        buy_dict: dict = {}          # 제품명:개수
        price_sum: float = 0

        print("구매할 수 있는 물품 목록")
        for i in range(len(shopping_list)):
            shopping_list[i] = shopping_list[i].split()
            shopping_dict[shopping_list[i][0].lower()]\
                = float(shopping_list[i][2])
            print("%-10s: %5s" % (shopping_list[i][0], shopping_list[i][2]))

        print("구매하실 물품과 개수를 입력해주세요. 상품명:개수, 상품명:개수")
        buy_list = input(">>>").lower().strip().split(",")
        for i in range(len(buy_list)):
            buy_list[i] = buy_list[i].strip().split(":")
            buy_dict[buy_list[i][0].strip()] = int(buy_list[i][1].strip())

        for i in list(buy_dict.keys()):
            price_sum += shopping_dict[i]*buy_dict[i]

        return price_sum

    except FileNotFoundError:
        # 인수로 전달된 파일이 존재하지 않을 때 발생하는 오류
        print("파일이 존재하지 않습니다.")
        return -1

    except ValueError:
        # 파일이나 입력창에서 숫자를 입력해야 할 곳에
        # 숫자가 아닌것을 입력하면 발생하는 오류
        print("파일이나 입력창에서 형식을 잘못 입력했습니다.")
        print("파일에서는 [상품명 개수 가격] 형태로,")
        print("입력창에서는 [상품명:개수, ...]형태로 입력해야 합니다.")
        return -1

    except KeyError:
        # 입력창에서 목록에 없는 품목을
        # 입력하면 발생하는 오류
        print("상품명을 잘못 입력했습니다.")
        return -1


def remove_elt(li: list) -> list:
    """
    리스트를 받아 중복값을 제거한 리스트를 리턴해주는 remove_elt(list) 함수를 구현하라.

    test) remove_elt(['a', 'a', 'b', 'c', 'd', 'b']) = ['a', 'b', 'c', 'd']
    """
    return_li: list = []

    for i in li:
        if not(i in return_li):
            return_li.append(i)

    return return_li


print("test1: fibo(5)=", fibo(5), "fibo(10)=", fibo(10))
print("==========================================")
print("test2: ", shopping_total_sum("Project01\shopping_list.txt"))
print("==========================================")
print("test3: ", remove_elt(['a', 'a', 'b', 'c', 'd', 'b']))
