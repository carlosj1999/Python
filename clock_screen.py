# Define the patterns for each digit
patterns = {
    '0': ["# # #", "#   #", "#   #", "#   #", "# # #"],
    '1': ["    #", "    #", "    #", "    #", "    #"],
    '2': ["# # #", "    #", "# # #", "#    ", "# # #"],
    '3': ["# # #", "    #", "# # #", "    #", "# # #"],
    '4': ["# #", "# #", "###", "  #", "  #"],
    '5': ["###", "#  ", "###", "  #", "###"],
    '6': ["###", "#  ", "###", "# #", "###"],
    '7': ["###", "  #", "  #", "  #", "  #"],
    '8': ["###", "# #", "###", "# #", "###"],
    '9': ["###", "# #", "###", "  #", "###"]
}

# Get the input from the user
number = input("Enter a number: ")

# Initialize a list to store the output lines
output_lines = ["", "", "", "", ""]

# Build the output using the patterns
for digit in number:
    for i in range(5):
        output_lines[i] += patterns[digit][i] + " "

# Print the output lines
for line in output_lines:
    print(line)
