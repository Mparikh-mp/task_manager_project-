# Week 5 - Lists and Dictionaries

tasks = ["Study Python", "Do assignment", "Practice coding"]
print("Task List:")

for task in tasks:
    print(task)

student = {
    "name": "John",
    "age": 20,
    "course": "Computer Science"
}

print("\nStudent Details:")
for key, value in student.items():
    print(key, ":", value)
