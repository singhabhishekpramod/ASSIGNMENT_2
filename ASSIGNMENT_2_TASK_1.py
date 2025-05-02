#Task 1: Check if a Number is Even or Odd
def check_even_odd():
    while True:
        try:
            num = int(input("Enter an integer: "))
            if num % 2 == 0:
                print(f"{num} is an even number.")
            else:
                print(f"{num} is an odd.")
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    check_even_odd()

if __name__ == "__main__":
    main()
