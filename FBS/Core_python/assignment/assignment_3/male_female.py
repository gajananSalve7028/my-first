
gender = input("Enter gender (male/female): ").lower()
age = int(input("Enter age: "))

if gender == "male" and age >= 21:
    print("Eligible by the given age condition")
elif gender == "female" and age >= 18:
    print("Eligible by the given age condition")
elif gender == "male" or gender == "female":
    print("Not eligible by the given age condition")
else:
    print("Invalid gender")
