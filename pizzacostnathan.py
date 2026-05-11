# Constants
HST = 0.13
LABOUR = 0.75
RENT = 1.00

# Input: Ask the user for the pizza diameter
# We use float() because the diameter can have decimals
diameter = float(input("What is the pizza diameter? "))

# Calculate Subtotal
materials = 0.5 * diameter
subtotal = LABOUR + RENT + materials

# Calculate Tax and Total
tax = subtotal * HST
total = subtotal + tax

# Show the result in the console
# We use f-strings to format the output to 2 decimal places
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")