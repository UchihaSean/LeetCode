def quick_sort(l):
    if len(l) <= 1:
        return l
    pivot = l[0]
    return quick_sort([x for x in l[1:] if x < pivot]) + [pivot] + quick_sort([x for x in l[1:] if x >= pivot])


def main():
    l = [0, 1, 5, 3, 2]
    print(quick_sort(l))


if __name__ == "__main__":
    main()
