# Ask the user to input a positive integer
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to go through each row
while row < size:
    # Use a for loop to print each asterisk in the current row
    for _ in range(size):
        print("*", end="")  # Stay on the same line
    print()  # Move to the next line after each row
    row += 1

