def factorial(n):
    """Computes recursively n! = 1 * 2 * ... * (n-1) * n
    """
    if n == 0:
        # Base case, 0! is by definition 1
        result = 1
    else:
        # Recursive case: n! = (n-1)! * n
        result = n * factorial(n-1)
    return result

def fibonacci(n):
    """Computes recursively the Fibonacci sequence
    F(n) = F(n-1) + F(n-2)
    for n > 2, with initial conditions F(1) = 1 and F(2) = 2
    """
    if n == 1 or n == 2:
        # Base case
        result = n
    else:
        # Recursive case
        result = fibonacci(n-1) + fibonacci(n-2)
    return result

# ITERATIVE VERSIONS OF ASSIGNMENT METHODS

def sum_of_digits_iterative(n):
    sum = 0
    while n > 1:
        # Obtain the last digit to add to sum
        sum += n % 10 
        # Remove the last digit
        n //= 10
    # Done
    return sum + n

def count_occurrences_iterative(data_list, target):
    count = 0
    for i in range(len(data_list)):
        if data_list[i] == target:
            count += 1
    return count


# WRITE YOUR CODE BELOW

