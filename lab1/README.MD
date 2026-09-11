## Name: Blaise Izerimana

## ID: 48452028

cs456-lab01/
│
├── data/
│ └── (optional: saved benchmark results or output datasets)
│
├── src/
│ ├── **init**.py
│ ├── algorithms.py  
│ ├── benchmark.py  
│ └── visualization.py  
│
├── plots/  
│ ├── mergesort_plot.png
│ ├── quicksort_plot.png
│ ├── linear_search_plot.png
│ ├── insertion_sort_plot.png
│ └── combined_comparison_plot.png
│
├── references.txt  
├── main.py  
├── requirements.txt  
└── README.md

    # Merge sort method from http://w3schools.com/python/trypython.asp?filename=demo_dsa_mergesort

def mergeSort(arr):
if len(arr) <= 1:
return arr

mid = len(arr) // 2
leftHalf = arr[:mid]
rightHalf = arr[mid:]

sortedLeft = mergeSort(leftHalf)
sortedRight = mergeSort(rightHalf)

return merge(sortedLeft, sortedRight)

def merge(left, right):
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

# mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]

# mysortedlist = mergeSort(mylist)

# print("Sorted array:", mysortedlist)

# Quick sort method from https://www.w3schools.com/Python/trypython.asp?filename=demo_dsa_quicksort

def partition(array, low, high):
pivot = array[high]
i = low - 1

for j in range(low, high):
if array[j] <= pivot:
i += 1
array[i], array[j] = array[j], array[i]

array[i+1], array[high] = array[high], array[i+1]
return i+1

def quicksort(array, low=0, high=None):
if high is None:
high = len(array) - 1

if low < high:
pivot_index = partition(array, low, high)
quicksort(array, low, pivot_index-1)
quicksort(array, pivot_index+1, high)

# mylist = [64, 34, 25, 5, 22, 11, 90, 12]

# quicksort(mylist)

# print(mylist)

# Linear search method from https://www.w3schools.com/Python/trypython.asp?filename=demo_dsa_linearsearch_index

def linearSearch(arr, targetVal):
for i in range(len(arr)):
if arr[i] == targetVal:
return i
return -1

# mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]

# x = 4

# result = linearSearch(mylist, x)

# if result != -1:

# print("Found at index", result)

# else:

# print("Not found")

# Insertion sort method from https://www.w3schools.com/Python/trypython.asp?filename=demo_dsa_insertionsort

def insertionSort(arr):
n = len(arr)
for i in range(1, n):
insert_index = i
current_value = arr.pop(i)
for j in range(i - 1, -1, -1):
if arr[j] > current_value:
insert_index = j
arr.insert(insert_index, current_value)
return arr

# mylist = [64, 34, 25, 12, 22, 11, 90, 5]

# insertionSort(mylist)

# print(mylist)
