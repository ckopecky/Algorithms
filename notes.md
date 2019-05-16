# How To Write and Analyze Problems

Important part is working through the problem. Only one extra point for the right answer. A million points for the process! 

First pass through on a possible solution to a problem will not necessary be the most performant. And that's okay! 

#### Time Complexity: 
-- a mathematical concept used to describe how well algorithms scale when the amount of data needed to process becomes very large. 

#### Space Complexity:

-- refers to the number of stack frames that it takes to run the algorithm. Recursion is more expensive space wise than an iterative solution because every time there is a recursive function call a new stack frame is added to stack. 

##### Write a program that checks to see if a list of integers contains a number: 

##### Iterative Solution

```py

def list_contains(l, x):
    i = 0
    while i < len(l):
        if l[i] == x:
            return True
        i += 1
    return False

list = [1, 2, 3, 4, 5]

list_contains(list, 3);

```

For every looping problem, there is probably a recursive solution. Why would we use one vs. the other? 

**Answer:** Whichever one is the most clear to read. 




##### Recursive Solution

Can I strip a base case off and then describe the problem in the same way with the remaining data? 

```py
def list_contains_recursion(l, x):
    # base case -- A WIN
    if l[0] == x:
        return True
    if l == []:
        return False
    return list_contains_recursions([1:], x)

list = [1, 2, 3, 4, 5]
list_contains_recursion(list, 3)
```

### Quicksort

list = [5, 7, 2, 9, 3, 8, 2, 6, 1]

first step: partition stack: takes a number from a list of numbers and calls it a pivot. 

second step: take the rest of the numbers and split them up into numbers less than pivot and numbers greater than pivot. 

2 3 1-----5-----7 9 8 6

left-----pivot-----right

third step: do the exact same thing with the left side and right side until sorted.

1------2------3

left--pivot--right

6---- 7 --- 9 8

left--pivot--right

6----7 ---8 9

```py
def quicksort(list):
    pivot = list[0]
    left = []
    right = []
    # you kinda want a pivot that's kinda in the middle. 
    i = 0
    while i < len(list):
        if(list[i] < pivot):
            left.append(list[i])

        else:
            right.append(list[i])

    # at this point we should have an array full of stuff less than pivot, the pivot and another array full of stuff greater than the pivot. 

    # this is recursion. It takes the left array and puts it into the quicksort function that we just wrote. Same with the right array.
    return quicksort(left) + pivot + quicksort(right)



```
Tree traversals benefit from recursion. 