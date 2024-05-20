# Define a list to store filtered pickup lines
filtered_lines = []

# Define a set to keep track of unique pickup lines
unique_lines = set()

# Read the pickup lines from the file
pickup_lines_file = 'NewAllPickupline.txt'
with open(pickup_lines_file, "r", encoding="utf-8") as file:
    all_lines = file.readlines()

# Iterate through each pickup line and remove the starting and ending double quotes
for line in all_lines:
    line = line.strip()
    # Remove starting and ending double quotes if present
    if line.startswith('"') and line.endswith('"'):
        print(line)
        line = line[1:-1]
    # Check if the line starts with a digit followed by a period and contains a space after that
    if line and line[0].isdigit() and '.' in line and line.index('.') == line.find(' ')-1:
        # Find the index of the first space after the period
        space_index = line.find(' ')
        # Extract the substring after the first space
        filtered_line = line[space_index+1:]
        if filtered_line not in unique_lines:
            filtered_lines.append(filtered_line)
            unique_lines.add(filtered_line)
    else:
        if line not in unique_lines:
            filtered_lines.append(line)
            unique_lines.add(line)

# Write the filtered lines to a new file
filtered_lines_file = 'newAllPickupline2.txt'
with open(filtered_lines_file, "w", encoding="utf-8") as file:
    file.write("\n".join(filtered_lines))

print("Filtered pickup lines saved to:", filtered_lines_file)
