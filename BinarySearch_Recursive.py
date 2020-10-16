import random

randArr = random.sample(range(10, 100), 30)

target = random.randint(10,80)

def bs_recursive(arr, l, h, key):

    if h >= l:

        mid = (h + l) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return bs_recursive(arr, l, mid - 1, key)
        else:
            return bs_recursive(arr, mid + 1, h, key)

    else:
        return -1


res = bs_recursive(randArr, 0, len(randArr) - 1, target)
if res != -1:
    print (f"The number {target} found at index {res} and it's value is {randArr[res]}.")
else:
    print (f'Your number {target} not found!')