def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Αναδρομική κλήση για κάθε μισό
        mergeSort(left)
        mergeSort(right)

        # Δύο δείκτες για τη διάσχιση των 2 μισών
        i = 0
        j = 0

        # Δείκτης για την κύρια λίστα
        k = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                # Η τιμή του αριστερού μισού εισάγεται στη λίστα
                myList[k] = left[i]
                i += 1
            else:
                # Η τιμή του δεξιού μισού εισάγεται στη λίστα
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # Για όλες τις τιμές που απομένουν
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1


myList = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(myList)
print(myList)
