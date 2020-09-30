import math
import os
import random
import re
import sys

#
# Complete the 'mostActive' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY customers as parameter.
#
from collections import Counter


def mostActive(customers):
    n = len(customers)
    custlist = []
    uniquecust = dict(zip(Counter(customers).keys(), Counter(customers).values()))
    for key in uniquecust.keys():
        if ((uniquecust[key]) // n) * 100 >= (5 // n) * 100:
            custlist.append(key)

    custlist.sort()
    print(custlist)
    return custlist


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    customers_count = int(input().strip())

    customers = []

    for _ in range(customers_count):
        customers_item = input()
        customers.append(customers_item)

    result = mostActive(customers)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
