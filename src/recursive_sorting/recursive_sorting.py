# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []

    #merge arrA and arrB in sorted order and return the array
    #checking if arrA < arrB
    arrAIndex = 0
    arrBIndex = 0

    while arrAIndex < len(arrA) and arrBIndex < len(arrB):
        if arrA[arrAIndex] <= arrB[arrBIndex]:
            merged_arr.append(arrA[arrAIndex])
            arrAIndex += 1
        else:
            merged_arr.append(arrB[arrBIndex])
            arrBIndex += 1

    while arrAIndex < len(arrA):
        merged_arr.append(arrA[arrAIndex])
        arrAIndex += 1

    while arrBIndex < len(arrB):
        merged_arr.append(arrB[arrBIndex])
        arrBIndex += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    #base case
    #if length of the arr (see parameter above) is <= 1
        #return the array
    if len(arr) <= 1:
        return arr
    #find the midpoint of the array like we did yesterday
    midpoint = len(arr) // 2
    #left spilt the array to the left half
    left = arr[:midpoint]
    #right spilt the array to the right half
    right = arr[midpoint:]
    #sort each half one at a time
    #recurse the left side with this function
    leftSorted = merge_sort(left)
    #recurse the right side with this function
    rightSorted = merge_sort(right)
    #merge both arrays
    #mergedArray = merge(leftSorted, rightSorted)
    mergedArray = merge(leftSorted, rightSorted)
    #arr = mergedArray
    arr = mergedArray
    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr

array = [9,7,8,3,2,1]
print(merge_sort(array))