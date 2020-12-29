
def swap(al, i, j):
    if(i != j):
        temp = al[i]
        al[i] = al[j]
        al[j] = temp


def partition(al, p, r):
    x = al[r]
    i = p-1
    for j in range(p, r):
        if(al[j] < x):
            i += 1
            swap(al, i, j)

    swap(al, i+1, r)
    return i+1


def quickSort(al, l, h):
    if(l < h):
        q = partition(al, l, h)
        quickSort(al, l, q-1)
        quickSort(al, q+1, h)


if __name__ == "__main__":
    al = [2, 4, 3, 6, 5, 8, 9, 1, 10, 12, 33, 22, 21]
    print(al)
    quickSort(al, 0, len(al)-1)
    print(al)
