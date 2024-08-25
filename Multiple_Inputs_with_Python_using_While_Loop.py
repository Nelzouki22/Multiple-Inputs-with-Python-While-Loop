# Initialize an empty list to store the inputs
user_inputs = []

# Set a flag to control the loop
continue_input = True

# Start the while loop
while continue_input:
    # Prompt the user for input
    user_input = input("Enter a value (or type 'done' to finish): ")

    # Check if the user wants to finish
    if user_input.lower() == 'done':
        continue_input = False
    else:
        # Add the input to the list
        user_inputs.append(user_input)

# Output the collected inputs
print("You entered:", user_inputs)

