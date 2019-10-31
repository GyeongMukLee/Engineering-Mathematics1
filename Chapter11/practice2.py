import math


exp1 = [math.exp(x) for x in range(1, 10, 2)]
# [2.718281828459045, 20.085536923187668, 148.4131591025766, 1096.6331584284585, 8103.083927575384]

exp2 = [math.exp(x) for x in range(3, 12, 3)]

print(exp1, exp2)
print(math.log(math.e))


def ReLu(x: int) -> int:
    if x <= 0:
        return 0
    else:
        return x


relu1 = [ReLu(x) for x in range(-10, 11)]
