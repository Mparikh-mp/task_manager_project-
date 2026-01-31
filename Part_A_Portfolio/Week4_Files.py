# Week 4 - File Handling

file = open("sample.txt", "w")
file.write("This is a sample file.\nPython file handling practice.")
file.close()

file = open("sample.txt", "r")
content = file.read()
file.close()

print("File Content:")
print(content)
