students = ["Thomas", "Joe", "Sophie"]
students.sort()
print(students)
first_name = students[0]
first_name = first_name[:-1]
print(first_name)
longest_name = ""
for name in students:
	if len(name) > len(longest_name):
		longest_name = name
print(longest_name)