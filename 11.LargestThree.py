def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    
    largest = find_largest(a, b, c)
    print(f"The largest number is {largest}.")

if __name__ == "__main__":
    main()
