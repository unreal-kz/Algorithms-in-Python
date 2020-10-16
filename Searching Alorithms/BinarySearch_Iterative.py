import random

rand_list = sorted(random.sample(range(100), 30), reverse=False)
key = random.randint(1,50)
# print(rand_list)


def bs_iter(arrList, target):

    low = 0
    high = len(arrList) - 1
    mid = 0

    while low <= high:
        mid = (low + high) // 2
        # print(mid)
        if arrList[mid] < target:
            low = mid + 1
        elif arrList[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1


print(f"The number you are looking for is {key} and it is found at index { bs_iter(rand_list,key) } ({rand_list[bs_iter(rand_list,key)]})")
