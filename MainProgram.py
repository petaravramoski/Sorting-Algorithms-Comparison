import random
import time


#importing algorithms from sorting_algorithms file
from sorting_algorithms import bubble_sort, bubble_sort2, bubble_sort3, bubble_sort4, SinkDownSort, BiDirectSort, selectionSort, insertionSort, quicksort, MergeSort, heap_sort


def menu():
    print("Please choose an option:")
    print("1. Test a single sorting algorithm")
    print("2. Test multiple sorting algorithms")
    print("3. Exit program")

#submenu that will appear if user selects option 1.
#This function allows the user to select 11 algorithms to run one at a time.
#The algorithms are called from the sorting_algorithms file, once the user has selected algorithm they want to run.
#The array size is entered by the user, and the numbers in the array are randomly generated. 
#The array and the amount of comparisons are also shown
def subMenu():
    print("1. Test selection sort algorithm")
    print("2. Test insertion sort algorithm")
    print("3. Test merge sort algorithm")
    print("4. Test quick sort algorithm")
    print("5. Test heap sort algorithm")
    print("6. Test bubble sort algorithm")
    print("7. Test Obs1-bubble sort algorithm")
    print("8. Test Obs2-bubble sort algorithm")
    print("9. Test Obs3-bubble sort algorithm")
    print("A. Test Sink-down sort algorithm")
    print("B. Test Bi-directional sort algorithm")

    sub_option = input("Enter the option you would like to choose: ")
    if sub_option == "1":
        print("You have selected Option 1: Test selection sort algorithm")
        n = int(input("Enter the size of the Array: "))
        A = [random.randint(0, n) for i in range(n)]
        Arr, comparisons = selectionSort(A, n)
        print("Number of comparisons:", comparisons)
    if sub_option == "2":
        print("You have selected Option 2: Test insertion sort algorithm")
        n = int(input("Enter the size of the Array: "))
        A = [random.randint(0, n) for i in range(n)]
        Arr, comparisons = insertionSort(A, n)
        print("Number of comparisons:", comparisons)
    if sub_option == "3":
        print("You have selected Option 3: Test merge sort algorithm")
        n = int(input("Enter the size of the Array: "))
        A = [random.randint(0, n-1) for i in range(n)]
        Arr , comparisons = MergeSort(A, n)
        print("Number of comparisons:", comparisons)
    if sub_option == "4":
        print("You have selected Option 4: Test quicksort algorithm")
        n = int(input("Enter the size of the Array: "))
        A = [random.randint(0, n-1) for i in range(n)]
        Arr, comparisons = quicksort(A, 0, n-1, n)
        print("Number of comparisons:", comparisons)
    if sub_option == "5":
        print("You have selected Option 5: Test heap sort algorithm")
        n = int(input("Enter the size of the Array: "))
        A = [random.randint(0, n-1) for i in range(n)]
        Arr, comparisons = heap_sort(A, n)
        print("Number of comparisons:", comparisons)
    if sub_option == "6":
        print("You have selected Option 6: Test bubble sort algorithm")
        n = int(input("Enter the size of the Array: "))
        A = [random.randint(0, n) for i in range(n)]
        Arr, comparisons = bubble_sort(A, n)
        print("Number of comparisons:", comparisons)
    if sub_option == "7":
        print("You have selected Option 7: Test bubble sort algorithm OBS1")
        n = int(input("Enter the size of the Array: "))
        A = [random.randint(0, n) for i in range(n)]
        Arr, comparisons = bubble_sort2(A, n)
        print("Number of comparisons:", comparisons)
    if sub_option == "8":
        print("You have selected Option 8: Test bubble sort algorithm OBS2")
        n = int(input("Enter the size of the Array: "))
        A = [random.randint(0, n) for i in range(n)]
        Arr, comparisons = bubble_sort3(A, n)
        print("Number of comparisons:", comparisons)
    if sub_option == "9":
        print("You have selected Option 9: Test bubble sort algorithm OBS3")
        n = int(input("Enter the size of the Array: "))
        A = [random.randint(0, n) for i in range(n)]
        Arr, comparisons = bubble_sort4(A, n)
        print("Number of comparisons:", comparisons)
    if sub_option == "A" or sub_option == "a": #case sensitive, user can enter A or a.
        print("You have selected Option A: Test Sink-down sort algorithm")
        n = int(input("Enter the size of the Array: "))
        A = [random.randint(0, n) for i in range(n)]
        Arr, comparisons = SinkDownSort(A, n)
        print("Number of comparisons:", comparisons)
    if sub_option == "B" or sub_option == "b": #case sensitive, user can enter B or b.
        print("You have selected Option B: Test Bi-directional sort algorithm")
        n = int(input("Enter the size of the Array: "))
        A = [random.randint(0, n) for i in range(n)]
        Arr, comparisons = BiDirectSort(A, n)
        print("Number of comparisons:", comparisons)


#Submenu2 that will appear if user selects option 2
def subMenu2():
    try:
        n = input("Enter the size of the array to be sorted (n>0): ")
        n = int(n)  # Convert the input to an integer

        if n <= 0:
            print("Invalid input, n must be greater than 0.")
            return

        # Generate the array of n integers
        A = [random.randint(0, n) for i in range(n)]

        algorithms = [bubble_sort, bubble_sort2, bubble_sort3, bubble_sort4, SinkDownSort, BiDirectSort, selectionSort, insertionSort, quicksort, MergeSort, heap_sort]

        #extracting the name of all functions using __name__ attribute
        sorting_algorithm_names = [function.__name__ for function in algorithms]

        array_sizes = [n]
        num_comparisons = []
        run_times_ms = []

        #for loop that runs all the algorithms, and uses the time module to calculate how long it takes to run each algorithm
        #Time is also turned into milliseconds 
        for algorithm in algorithms:
            start_time = time.time()
            #if statement to make sure the quciksort, merge sort works correctly as they need different parameters 
            if algorithm.__name__ in ["quicksort"]:
                sorted_array, comparisons = algorithm(A[:], 0, n-1, n)
            else:
                sorted_array, comparisons = algorithm(A[:], n)
            end_time = time.time()
            #time in milliseconds 
            run_time_ms = round((end_time - start_time) * 1000, 2)

            num_comparisons.append(comparisons)
            run_times_ms.append(run_time_ms)

        #take information from above and store in table var so that the table can be generated
        table = generate_table(sorting_algorithm_names, array_sizes, num_comparisons, run_times_ms)
        print(table)


    except ValueError:
        print("Invalid input, please enter an integer number.")

#Function to generate the table
def generate_table(sorting_algorithm_names, array_sizes, num_comparisons, run_times_ms):

    # Define headers for the table
    headers = ['Sorting algorithm name', 'Array size', 'Num. of Comparisons', 'Run time (in ms.)']

    # Generate the table
    table = '{:<25} {:<15} {:<25} {:<20}\n'.format(*headers)  # header row
    # Loop through the sorting algorithm names and their corresponding statistics
    for i in range(len(sorting_algorithm_names)):
        # Add a row to the table for each sorting algorithm
        table += '{:<25} {:<15} {:<25} {:<20}\n'.format(sorting_algorithm_names[i], array_sizes[0], num_comparisons[i], run_times_ms[i])

    return table


option = 0

while option != 3:
    try:
        menu()
        option = int(input("Enter the option you would like to choose: "))
        if option == 1:
            print("You have selected Option 1: Test a single sorting algorithm")
            subMenu()
        elif option == 2:
            print("You have selected Option 2: Test multiple sorting algorithms") 
            subMenu2()
        elif option == 3:
            print("Exiting program...")
            break
        else:
            print("Invalid input, please enter 1, 2, or 3.")
        
    except ValueError:
        print("Invalid input, please enter a number.")

