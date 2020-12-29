def merge(al, low, mid, high):
    L = al[low:mid+1]
    R = al[mid+1:high+1]

    # print(L, "         ", R)

    i, j, k = 0, 0, low
    while(i < len(L) and j < len(R)):
        if(L[i] <= R[j]):
            al[k] = L[i]
            i += 1
        else:
            al[k] = R[j]
            j += 1
        k += 1

    while(i < len(L)):
        al[k] = L[i]
        k += 1
        i += 1
    while(j < len(R)):
        al[k] = R[j]
        k += 1
        j += 1


def mergeSort(al, low, high):
    if(low < high):
        mid = int((low+high)/2)
        mergeSort(al, low, mid)
        mergeSort(al, mid+1, high)
        merge(al, low, mid, high)


if __name__ == "__main__":
    al = [2, 4, 3, 6, 5, 8, 9, 1, 10, 12, 33, 22, 21]
    print(al)
    mergeSort(al, 0, len(al)-1)
    print(al)
