name = input("Enter student name: ")

python = int(input("Python Marks: "))
html = int(input("HTML Marks: "))
css = int(input("CSS Marks: "))

total = python + html + css
average = total / 3

print("\n----- Result -----")
print("Name    :", name)
print("Total   :", total)
print("Average :", average)

if average >= 90:
    print("Grade : A")
elif average >= 75:
    print("Grade : B")
elif average >= 50:
    print("Grade : C")
else:
    print("Grade : Fail")