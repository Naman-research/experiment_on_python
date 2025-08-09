spam_words = ["click now", "earn money", "free money", "fucking", 
              "bastard", "money", "click", "discount"]

# Step 1: Read the file
with open("spam_file.txt", "r") as f:
    lines = f.readlines()

# Step 2: Process lines
new_lines = []
for line in lines:
    lowered_line = line.lower()
    for spam in spam_words:
        if spam in lowered_line:
            line = line.replace(spam, "####")
            lowered_line = line.lower()  # update lowercase version
    new_lines.append(line)

# Step 3: Write back to the file
with open("spam_file.txt", "w") as f:
    f.writelines(new_lines)
