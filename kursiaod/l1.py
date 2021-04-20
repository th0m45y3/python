#функция преобразования бинарного дерева в кучу(сортировка)
def heapify(a, n, i):
    mah = i
    l = 2*i+1
    r = 2*i+2
    if l<n and a[i]<a[l]:
        mah = l
    if r<n and a[mah]<a[r]:
        mah = r
    if mah!=i:
        a[i],a[mah]=a[mah],a[i]
        heapify(a, n, mah)

#функция сортировки кучи        
def heapSort(a):
    n = len(a)
    for i in range(n, -1, -1):
        heapify(a, n, i)
    for i in range (n-1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapify(a, i, 0)

#функция сортировки отельной части массива
def partition(arr, low=0, high=None):
    if high == None: high = len(arr)
    i = (low-1)       
    pivot = arr[high]    
    for j in range(low, high):  
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

#функция быстрой сортировки («прыжками» в разные стороны)
def quickSort(arr, low=0, high=None):
    if high == None: high = len(arr)-1
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

#сортировка каждой строки массива
def matrixSort(a, func):
    for i in range(len(a)):
        func(a[i])

#основная функция
import random, time
mat = [[random.randint(0, 100) for x in range(100)] for k in range(1000)]
copy = mat
#print("Generated array:")
#for row in mat: print(row)
t = time.time()
matrixSort(mat, heapSort)
t = time.time() - t
print(f"HeapSort execution time: {1000*t} milliseconds")
#print("\nSorted array by heapSort:")
#for row in mat: print(row)

mat = copy
t = time.time()
matrixSort(mat, quickSort)
t = time.time() - t
print(f"QuickSort execution time: {1000*t} milliseconds")
#print("\nSorted array by quickSort:")
#for row in mat: print(row)

mat = copy
t = time.time()
matrixSort(mat, sorted)
t = time.time() - t
print(f"Sorted execution time: {1000*t} milliseconds")
#print("\nSorted array by Python sorted():")
#for row in mat: print(row)
