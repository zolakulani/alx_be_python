"""
pattern_drawing.py
Draws a square pattern of asterisks based on user input size.
Uses a while loop with nested for loop.
"""


size = int(input("Enter the size of the pattern: "))

# Validate that size is positive
if size <= 0:
    print("Please enter a positive integer.")
    
# Initialize row counter
row = 0

# Use while loop for rows
while row < size:
    # Use for loop for columns within each row
    for _ in range(size):
        print("*", end="")
    
    # Move to next line after completing a row
    print()
    
    # Increment row counter
    row += 1
    
