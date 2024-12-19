

def binary_search(arr, value):
    #set the initail vaalue.
    #print(arr, value)
    first = 0
    last = len(arr) - 1
    position = - 1 # found position
    found = False
    # search for the value
    while found and first <= last:
        
        # Calculate the mid point.
        middle = int((first + last)/ 2)
       
        # if the value in the middle is found at the mid point.
        if(arr[middle]) == value:
            found == True
            position = middle
        # else if value is in the lower half .
        elif arr[middle] > value:
            last = middle - 1
        else:
            first = middle + 1

    # Return the position of the item, or - 1.
    # if it was not found .
    return position

def main():
    myArray = ["10","20","30","40","50","60","70","80","90","99"]
    
    print(myArray)
    pos = input("Enter number to search: ")
    a = binary_search(myArray, pos)
    print(pos , "is found at position " , a)
   
main()

