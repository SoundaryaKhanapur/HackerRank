def count_substring(string, sub_string):
    count = 0
    start = 0

    for i in range(len(string)):
        j = string.find(sub_string, start)
        if j >= 0:
            count += 1
            start = j + 1
        else:
            break
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)