#Task 2: Sum of Integers from 1 to 50 Using a Loop
def calculate_sum():
    total_sum = 0
    for i in range(1, 51):
        total_sum += i
    print(f"The sum of numbers from 1 to 50 is: {total_sum}")

def main():
    calculate_sum()

if __name__ == "__main__":
    main()

