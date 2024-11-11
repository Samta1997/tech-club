

# Program to check number is even odd or prime
def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def main():
    number = int(input("Enter a number: "))
    
    # Check if the number is odd or even
    odd_even = check_odd_even(number)
    print(f"The number is {odd_even}.")
    
    # Check if the number is prime
    if check_prime(number):
        print(f"The number {number} is prime.")
    else:
        print(f"The number {number} is not prime.")

if __name__ == "__main__":
    main()
