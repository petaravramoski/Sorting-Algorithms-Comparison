#**************bubble***************
def bubble_sort(A, n):
    comparisons = 0 #comparison counter
    for k in range(0, n-1): # Iterate through the array n-1 times, where n is the length of the array,
        for i in range(0, n-1):
            comparisons += 1 #for each comparison increment 
            if A[i] > A[i+1]:  #Comparing the indexes
                A[i], A[i+1] = A[i+1], A[i] #swapping the indexes 
    return A, comparisons

#**************bubble2***************
def bubble_sort2(A, n):
    comparisons = 0 #comparison counter
    for k in range(0, n-1): # Iterate through the array n-1 times, where n is the length of the array
        for i in range(0, n-k-1): # The inner loop ends at n-k-1 because the k largest elements are already in their correct positions
            comparisons += 1 #for each comparison increment 
            if A[i] > A[i+1]: #Comparing the indexes
                A[i], A[i+1] = A[i+1], A[i] #swapping the indexes 
    return A, comparisons


#**************bubble3***************
def bubble_sort3(A, n):
    comparisons = 0
    for k in range(0, n-1):
        flag = 0
        for i in range(0, n-1):
            comparisons += 1
            if A[i] > A[i+1]: #Comparing the indexes
                A[i], A[i+1] = A[i+1], A[i] #swapping the indexes 
                flag = 1 #if flag = 1 then continue the program as the array is not sorted 
        if flag == 0: #if flag == 0 that means its all sorted and it will terminate early (no swaps wore made)
            break
    return A, comparisons

#**************bubble4***************
#Essentially the same comments as the functions above
def bubble_sort4(A, n):
    comparisons = 0
    for k in range(0, n-1):
        flag = 0
        for i in range(0, n-k-1):
            comparisons += 1
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                flag = 1
        if flag == 0:
            break
    return A, comparisons

#**************sink***************
def SinkDownSort(A, n):
    comparisons = 0
    for k in range(n-1, 0, -1): #decrement by 1 as sink down sort goes backwards 
        flag = 0
        for i in range(0, k): 
            comparisons += 1
            if A[i] > A[i+1]: #comparing indexes 
                A[i], A[i+1] = A[i+1], A[i] #swapping indexes 
                flag = 1 #if flag = 1 then continue the program as the array is not sorted 
        if flag == 0: #if flag == 0 that means its all sorted and it will terminate early (no swaps wore made)
            break
    return A, comparisons

#**************bidirectsort***************
def BiDirectSort(A, n):
    comparisons = 0
    for k in range(n//2): #The array is split into two sub arrays and the sorting for each sub array will be performed during each iteration 
        left_flag = False
        right_flag = False
        for i in range(k, n-k-1): #scan left
            if A[i] > A[i+1]: #comparing the first half of the indexes 
                A[i], A[i+1] = A[i+1], A[i] #swapping the indexes 
                left_flag = True
                comparisons += 1
        for i in range(n-k-2, k, -1): #scan right 
            if A[i] < A[i-1]: #comparing the second half of the indexes 
                A[i], A[i-1] = A[i-1], A[i] #swapping the indexes 
                right_flag = True
                comparisons += 1
        if not left_flag and not right_flag: #checking if any swaps wore made if not then break (terminate early)
            break
    return A, comparisons

#**************selection***************
def selectionSort(A, n):
    comparisons = 0 #comparison counter
    for i in range(0, n-1): #iterate over the array except the last element
        imin = i  #set the index of the minimum value to the current index i
        for j in range(i+1, n): #iterate over the remaining unsorted elements in the array
            if A[j] < A[imin]: #compare the value of the current element to the minimum value
                imin = j #if current element is less than minimum value, update index of minimum value
            comparisons += 1 #increment comparison counter for each comparison made
        A[i], A[imin] = A[imin], A[i] #swap indexes 
    return A, comparisons
        
#**************insertion***************        
def insertionSort(A, n):
    comparisons = 0 #comparison counter
    for i in range(1, n): #iterate through the array starting from the second element
        value = A[i] #set the value of the current element
        hole = i #set the index of the current element 
        while(hole > 0 and A[hole-1] > value): #compare the value with the elements to the left
            A[hole] = A[hole-1] #shift the greater elements to the right
            hole = hole - 1 #decrement the hole index
            comparisons += 1 #increment the comparison counter
        A[hole] = value #insert the value in the correct position
    return A, comparisons


#**************quick sort***************
def partition(A, start, end):
    pivot = A[end] #Selecting the pivot element as the last element in the array
    pindex = start #Initializing the pivot index to the start of the array
    comparisons = 0 #Initializing the comparison counter
    for i in range(start, end): #Iterating over the array from start to end
        comparisons += 1 #Incrementing the comparison counter for each comparison
        if A[i] <= pivot:  #If the current element is less than or equal to the pivot element
            A[i], A[pindex] = A[pindex], A[i] #Swap the current element with the element at pivot index
            pindex += 1 
    A[end], A[pindex] = A[pindex], A[end] #Finally, swap the pivot element with the element at pivot index
    return pindex, comparisons

def quicksort(A, start, end, n):
    comparisons = 0 #Initializing the comparison counter
    if start < end: #If there are more than one elements in the array
        pindex, comp1 = partition(A, start, end) #Perform partitioning and get the pivot index and the number of comparisons made
        comparisons += comp1 #Add the number of comparisons made during partitioning to the total comparison count
        quicksort(A, start, pindex-1, n) #Recursively sort the left sub array (its recursive because we are calling the quicksort function within itself)
        quicksort(A, pindex+1, end, n) #Recursively sort the right sub array
    return A, comparisons
#***************************************


#**************merge sort***************
def merge(L,R,A):
    nL = len(L) #length of left subarray
    nR = len(R)  #length of right subarray
    j, i, k = 0, 0, 0 #initialize indices for left, right and merged arrays
    num_comparisons = 0  #counter variable for comparisons
    while(i < nL and j < nR): #merge until either subarray cant anymore
        num_comparisons += 1  #increment counter for comparison
        if(L[i] <= R[j]): #compare left and right elements
            A[k] = L[i] #copy smaller element to merged array
            i+=1 #move to next element in left subarray
        else:
            A[k] = R[j] #copy smaller element to merged array
            j+=1 #move to next element in right subarray
        k+=1 
    while(i < nL): #copy remaining elements in left subarray
        A[k] = L[i]
        i+=1 
        k+=1 
    while(j < nR): #copy remaining elements in right subarray
        A[k] = R[j]
        j+=1 
        k+=1 
    return num_comparisons

def MergeSort(A, n):
    num = len(A) #length of input array
    if(num < 2):
        return A, 0  #return 0 comparisons for single element arrays
    mid = num // 2  #calculate midpoint of input array entered by user
    left = []
    right = []
    for i in range(0, mid):
        left.append(A[i])
    for i in range(mid, n):
        right.append(A[i])
    left, lcomp = MergeSort(left, len(left)) #recursively sort left subarray
    right, rcomp = MergeSort(right, len(right)) #recursively sort right subarray
    merge_comp = merge(left, right, A) #merge sorted left and right subarrays
    num_comparisons = lcomp + rcomp + merge_comp #total comparisons made in this sorting operation
    return A, num_comparisons
#***************************************

#**************heap sort***************
def heap_sort(arr, n):
    comparisons = 0
    
    #Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, comparisons)
    
    #Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] #swap
        heapify(arr, i, 0, comparisons)
    
    return arr, comparisons

def heapify(arr, n, i, comparisons):
    largest = i #Initialize largest as root
    left = 2 * i + 1 #left child
    right = 2 * i + 2 #right child
    
    #if left child is larger than root
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    #if right child is larger than largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    #if largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # swap
        comparisons += 1
        heapify(arr, n, largest, comparisons)
#***************************************
