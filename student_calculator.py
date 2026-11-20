name = input("Enter your name: ")
while True:
    mathematics = int(input("Enter your Mathematics score: "))
    if mathematics < 0 or mathematics > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
    else:
        break
while True:
    english = int(input("Enter your English score: "))
    if english < 0 or english > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
    else:
        break
while True:
    physics = int(input("Enter your Physics score: "))
    if physics < 0 or physics > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
    else:
        break
while True:
    chemistry = int(input("Enter your Chemistry score: "))
    if chemistry < 0 or chemistry > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
    else:
        break

total = mathematics + english + physics + chemistry
average = total / 4

print(f"Name: {name}")
print(f"Total: {total}")
print(f"Average: {average}")
if average >= 70 and average <= 100:
    print(f"{name} your grade is: A")
elif average >= 60 and average < 70:
    print(f"{name} your grade is: B")
elif average >= 50 and average < 60:
    print(f"{name} your grade is: C")
elif average >= 45 and average < 50:
    print(f"{name} your grade is: D")
elif average < 0 or average > 100:
    print(f"{name} your grade is: Invalid, Because the average is less or above the required range")
else:
    print(f"{name} your grade is: F")

