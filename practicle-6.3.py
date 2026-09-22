# Write data to the file
file = open("practicle-6.3.txt", "w")
file.write("Hello, my name is Khush.\n")
file.close()

# Append additional data to the same file
file = open("practicle-6.3.txt", "a")
file.write("I am learning file handling.\n")
file.close()

# Display the contents of the file
file = open("practicle-6.3.txt", "r")
print(file.read())
file.close()