"""Implement a function recursively to get the desired
Fibonacci sequence value.
Your code should have the same input/output as the 
iterative code in the instructions."""

def get_fib(position):
    if position <= 1:
        return position
    return get_fib(position - 1) + get_fib(position - 2)

def get_fib_efficient(position):
    a = [0,1]
    for i in range(2, position + 1):    
        a.append(a[i - 1] + a[i - 2])
    return a[position]

# Test cases
print(get_fib(9))
print(get_fib(11))
print(get_fib(0))
