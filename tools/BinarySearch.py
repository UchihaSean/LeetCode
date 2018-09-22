def binary_search(s, val):
    # (l, r]
    l = -1
    r = len(s) - 1
    while l + 1 < r:
        mid = (l + r) / 2
        if s[mid] >= val:
            r = mid
        else:
            l = mid
    left = r

    # [l, r)
    l = 0
    r = len(s)
    while l + 1 < r:
        mid = (l + r) / 2
        if s[mid] <= val:
            l = mid
        else:
            r = mid
    right = l
    return left, right


def main():
    s = [2, 2, 2, 2, 2, 2]
    print(binary_search(s, 2))


if __name__ == "__main__":
    main()
