def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

print(flatten_and_sort([[3, 2, 1], [7, 9, 8], [6, 4, 5]]))

#How does this solution ensure data immutability?
#It ensures that the input array is not mutated

#Is this solution a pure function? Why or why not?
#no, it is not pure because it modifies the input array

#Is this solution a higher order function? Why or why not?
#Yes, it is a higher order function because it takes another function as an argument (sorted) and returns a new function (flatten_and_sort)

#Would it have been easier to solve this problem using a different programming style?
#This seems pretty simple to me.

#Why in particular is functional programming a helpful paradigm when solving this problem?
#Because it is easier to read and understand