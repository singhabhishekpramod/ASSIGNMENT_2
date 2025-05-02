#Task 1: Check if a Number is Even or Odd
def check_even_odd():
    while True:
        try:
            num = int(input("Enter an integer: "))
            if num % 2 == 0:
                print(f"{num} is even.")
            else:
                print(f"{num} is odd.")
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    check_even_odd()

if __name__ == "__main__":
    main()
