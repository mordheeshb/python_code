# Sorting Programs

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# 1. Student Marks Sorting
print(bubble_sort([75, 90, 65, 85, 70]))

# 2. Product Price Sorting
print(bubble_sort([1200, 500, 2500, 800]))

# 3. Student Ranking
print(selection_sort([88, 72, 95, 60, 81]))

# 4. Book ID Sorting
print(selection_sort([104, 101, 109, 102]))

# 5. Employee Age Sorting
print(selection_sort([35, 28, 42, 25, 31]))

# 6. Card Sorting
print(insertion_sort([7, 3, 9, 1, 5]))

# 7. Entered Marks Sorting
print(insertion_sort([60, 50, 70, 40]))

# 8. Contact Number Sorting
print(insertion_sort([9876, 4567, 1234, 7890]))

# 9. Student Record Sorting
print(merge_sort([55, 12, 89, 34, 23, 78]))

# 10. Customer Account Sorting
print(merge_sort([5678, 1234, 8901, 3456]))

# 11. Product Search Result Sorting
print(quick_sort([1000, 200, 1500, 500, 800]))

# 12. Cricket Score Sorting
print(quick_sort([45, 78, 23, 90, 67]))

# 13. Employee Salary Sorting
print(selection_sort([45000, 30000, 60000, 25000]))

# 14. Railway Ticket Sorting
print(selection_sort([567, 123, 789, 345]))

# 15. Patient ID Sorting
print(selection_sort([205, 101, 309, 150]))

# 16. Roll Number Sorting
print(selection_sort([25, 12, 30, 18]))

# 17. Nearly Sorted Data
print(insertion_sort([10, 20, 30, 25, 40]))

# 18. Customer ID Merge
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))

# 19. Sports Score Sorting
print(quick_sort([120, 95, 150, 80, 110]))

# 20. Large Dataset Sorting
print(merge_sort([99, 12, 45, 67, 23, 89, 34]))
