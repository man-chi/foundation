def custom_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def main():
    # Example usage of the custom_sum function
    numbers = [1, 2, 3, 4, 5]
    print(f"The sum of {numbers} is {custom_sum(numbers)}")

if __name__ == "__main__":
    main()
