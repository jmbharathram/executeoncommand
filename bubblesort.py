def displayList(arr):
  surround_arr = ["--" for num in arr]
  surround_arr = "-----" + '--'.join(surround_arr) + "----"
  arr = [str(num) for num in arr]
  array = "| " + ' | '.join(arr) + " |"
  print(surround_arr)
  print(array)
  print(surround_arr)

def displayIndex(arr, j):
  arr = [" " for num in arr]
  arr[j] = "\u2191"
  arr_str1 = "   " + '    '.join(arr) + "   "
  print(arr_str1)
  arr[j] = "j"
  arr[j+1] = "j+1"
  arr_str2 = "   " + '    '.join(arr)
  print(arr_str2)


def bubble_sort(mylist): 
    n = len(mylist)
    count = 0
    swap = True 

    print("Initial List: ")
    displayList(mylist)
    print()
  
    for i in range(n-1):
      if swap:
        swap = False 
        print()
        print(f"Iteration# {i+1}")
        for j in range(0, n-i-1):
            displayList(mylist)
            displayIndex(mylist,j)
            count = count + 1
            print()
            print(f"Step# {count}")
            print()
            if mylist[j] > mylist[j+1] :
                print()
                print(f"{mylist[j]} is greater than {mylist[j+1]}.") 
                print(f"Swap - {mylist[j]} \u2194 {mylist[j+1]}")
                print()
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j] 
                swap = True

        displayList(mylist)

mylist = [19, 23, 10, 19, 32, 60, 87]  
bubble_sort(mylist) 

'''
(n-1) + (n-2) + (n-3) + ..... + 3 + 2 + 1

sum of a sequence (n values) = n*(n+1)/2

Sum = n(n-1)/2 = (n^2 - n)/2
i.e O(n^2) / O(1)
'''
