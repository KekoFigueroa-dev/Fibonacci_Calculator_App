# Fibonacci Calculator App - Calculates Fibonacci sequence and demonstrates Golden Ratio convergence
print("Welcome to my Fibonacci Calculator App! IF you test it, I'll give you a Dinosaur")

# Input validation loop - Ensures positive integer input
while True:
    try:
        fib_input=int(input("How many digits of the Fibonacci Sequence would you like to compute: "))
        if fib_input <= 0:
            print("Please enter a positive number")
            continue
        break
    except ValueError:
        print("Please enter a Valid integer!")


# Initialize sequence with first two Fibonacci numbers
fib_list = [1, 1]

# Generate Fibonacci sequence by adding previous two numbers
for i in range(fib_input - 2):
    fib_seq = fib_list[-1] + fib_list[-2]
    fib_list.append(fib_seq)

# Display Fibonacci sequence
print(f"The first {fib_input} numbers of the Fibonacci sequence are: \n")
# Loop through sequence to display each number
for number in fib_list:
    print(number)

# Calculate ratios between consecutive numbers to demonstrate Golden Ratio
fib_ratios = []
for i in range(1, len(fib_list)):
    ratio = fib_list[i] / fib_list[i-1]
    fib_ratios.append(ratio)

# Display Golden Ratio values
print("\nThe corresponding Golden Ratio values are: ")
for ratio in fib_ratios:
    print(ratio)


print("\nThe ratio of consecutive Fibonacci terms approaches Phi; 1.618...")

# ASCII MotherEffing Dinosaur!

print("Thank you for testing my App :) Here's a Dinosaur ")
print("               __")
print("              / _)")
print("     _.----._/ /")
print("    /         /")
print(" __/ (  | (  |")
print("/__.-'|_|--|_|")
