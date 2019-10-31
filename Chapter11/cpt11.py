# 리스트 1
odd_list1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(odd_list1)

# 리스트 2
i = 0
odd_list2 = []
while i < 20:
    if i % 2 == 1:
        odd_list2.append(i)
    i += 1

print(odd_list2)

# 리스트 3
odd_list3 = []
for i in range(21):
    if(1 % 2 == 1):
        odd_list3.append(i)


# 리스트 4
def odd_number(num: int) -> list:
    return_value = []
    for i in range(num+1):
        if(i % 2 == 1):
            return_value.append(i)
    return return_value


print(odd_number(20))

odd_list4 = [x for x in range(100000+1) if x % 2 == 1]

square = [x**2 for x in range(100000+1)]
print(square[:20])
