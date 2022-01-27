def selection_sort(a, n, i):
    if n == i:
        return
    else:
        pmin = i
        for j in range(i + 1, n):
            if a[j] < a[pmin]:
                pmin = j

        temp = a[i]
        a[i] = a[pmin]
        a[pmin] = temp

        selection_sort(a, n, i + 1)


if __name__ == "__main__":
    a = [3, 4, 1, 7, 9, 2, 6]
    selection_sort(a, len(a), 0)
    print(a)
