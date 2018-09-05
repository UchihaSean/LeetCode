

def merge(a1, n1, a2, n2, a, n, count1, count2):
    c = c1 = c2 =0
    count = [0 for i in range(n)]

    while c < n:
        if c1 == n1:
            while c < n:
                a[c] = a2[c2]
                count[c] = count2[c2]
                c = c + 1
                c2 = c2 + 1
        elif c2 == n2:
            while c < n:
                a[c] = a1[c1]
                count[c] = count1[c1]
                c = c + 1
                c1 = c1 + 1
        else:
            if a1[c1] > a2[c2]:
                a[c] = a2[c2]
                count[c] = count2[c2]+n1-c1
                c = c + 1
                c2 = c2 + 1
            else:
                a[c] = a1[c1]
                count[c] = count1[c1]
                c = c + 1
                c1 = c1 + 1
    return count

def Sort(a, count):
    n = len(a)
    if n == 1: return [0]
    n1 = n/2
    n2 = n - n1
    a1 = a[:n1]
    a2 = a[n1:]
    count1 = Sort(a1, count[:n1])
    count2 = Sort(a2, count[n1:])
    # print count1,count2
    c = c1 = c2 = 0
    new_count = merge(a1, n1, a2, n2, a, n, count1, count2)
    return new_count


array = [1,2,4,3,2,1]
count = [0 for i in range(len(array))]
new_count = Sort(array,count)
print max(new_count)