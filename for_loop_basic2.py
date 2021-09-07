# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def BiggieSize(xyz):
    for num in range(len(xyz)):     #for num in xyz:  ??
        if xyz[num]<0:
            xyz[num]="big"

a=[1,-1,1,-1,1] 
print(a)  
BiggieSize(a)       #in JavaScript I remember i couldn't modify the original list, am I wrong?
print(a)

# THE CODE BELOW WOULDN'T WORK - WHY?

def BiggieSize(donut):
    for d in donut:
        if d<0:
            print(d)
            d="big"  #ok, I guess this screws up the for loop?
            print(d)
    print(donut)
    return donut

a=[1,-1,1,-1,1] 
print(a)  
b=BiggieSize(a)       
print(a)
print(b)


# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

def countPositives(donut):
    numberOfPositives=0
    for d in range(len(donut)):
        if donut[d]>0:
            numberOfPositives+=1 
    donut[len(donut)-1]=numberOfPositives
    return donut

#DOING THIS REQUIRES A RETURN STATEMENT
a=[1,-1,1,-1,1,6,7,1] 
print(a)
b=countPositives(a)
print(a)
print(b)

#DOING THIS DOES NOT REQUIRE A RETURN STATEMENT
a=[1,-1,1,-1,1,6,7,1] 
print(a)
countPositives(a)
print(a)


def countPositives(donut):
    numberOfPositives=0
    for d in donut:
        if d>0:
            numberOfPositives+=1  
    donut[len(donut)-1]=numberOfPositives
    return donut

a=[1,-1,1,-1,1] 
countPositives(a)

a=[1,-1,1,-1,1,6,7,1] 
print(a)
b=countPositives(a)
print(a)
print(b)

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

def SumTotal(xyz):
    sum = 0
    for x in range(len(xyz)):
        sum+=xyz[x]
    return sum

a=[1,2,3,4]
b=SumTotal(a)
print(a)
print("Sum total is",b)


# Average - Create a function that takes a list and returns the average of all the values.
# Example: average([1,2,3,4]) should return 2.5

def findAverage(xyz):
    sum=0
    for x in range(len(xyz)):  
        sum=sum+xyz[x]
    avg=sum/len(xyz)
    print("List =",xyz)
    return(avg)

a=[1,2,3,4]
b=findAverage(a)
print("Average is",b)


# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

# isn't this redundant?
def lengthOfList(xyz):
    return len(xyz)

a=[1,2,3,4]
b=lengthOfList(a)
print(a)
print("Length of list is",b)

######pretend I don't know len()

def lengthOfList(xyz):
    length=0
    for x in xyz:
        length+=1
    return length
a=[1,2,3,4]
b=lengthOfList(a)
print(a)
print("Length of list is",b)


# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

def miniMum(xyz):
    if len(xyz)==0:
        return False
    else:
        min=xyz[0]
        for x in range(len(xyz)):
            if min>xyz[x]:
                min=xyz[x]
        return min

a=[1,2,3,4,5,-3,-2,-2,0]
b=miniMum(a)
print("list =",a)
print("Minimum =",b)

a=[]
b=miniMum(a)
print("list =",a)
print("Minimum =",b)


# Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

def maxiMum(xyz):
    if len(xyz)==0:
        return False
    else:
        max=xyz[0]
        for x in range(len(xyz)):
            if max<xyz[x]:
                max=xyz[x]
        return max

a=[1,2,3,4,5,-3,-2,-2,0]
b=maxiMum(a)
print("list =",a)
print("Maximum =",b)

a=[]
b=maxiMum(a)
print("list =",a)
print("Maximum =",b)


# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimateAnalysis(xyz):
    results={}
    sumTotal = 0
    min=xyz[0]
    max=xyz[0]

    for x in range(len(xyz)):

        sumTotal+=xyz[x]

        if min>xyz[x]:
            min=xyz[x]

        if max<xyz[x]:
            max=xyz[x]

    avg=sumTotal/len(xyz)
    results["sumTotal"]=sumTotal
    results["average"]=avg
    results["minimum"]=min
    results["maximum"]=max
    results["length"]=len(xyz)
    return results

aaaa=[37,2,1,-9]   #THIS GETS A SYNTAX ERROR IN THE TERMINAL BUT NOT IN VS CODE
bbbb=ultimateAnalysis(aaaa)
print(bbbb)



# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(xyz):
    xyz.reverse()
    return(xyz)

a=[37,2,1,-9]
print(a)
b=reverse_list(a)
print(b)

# ok, pretend I don't know .reverse()

def reverse_list(xyz):
    for x in range(len(xyz)//2):
        xyz[x],xyz[len(xyz)-1-x]=xyz[len(xyz)-1-x],xyz[x]

a=[37,2,1,-9]
print(a)
reverse_list(a)
print(a)