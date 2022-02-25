# Student Name: Ayush Singh

# Description: Recursively find the sum and the product of all the digits in an integer.

# Add two integer values
def add(x, y):
    return x + y


# Multiply two integer values
def mult(x, y):
    return x * y


# Process every digit and perform the respective operation
def process_digits(n, operation):
    # Base case: If n // 10 = 0 (n is the last digit in the number), return n
    if n // 10 == 0:
        return n
    # Run the operation with parameters "n % 10" and the function process_digits recursively.
    return operation(n % 10, process_digits((n // 10), operation))


def main():
    value = int(input("Enter Your Number: "))
    print("Sum of all digits in", value, ":", process_digits(value, add))
    print("Product of all digits in", value, ":", process_digits(value, mult))


if __name__ == '__main__':
    main()
