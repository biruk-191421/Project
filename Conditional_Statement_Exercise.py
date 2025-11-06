# Age Classification Function; Create a function named classify_person 
#that takes a person's age as input. the function must use conditional 
#statements to classify theage into one of four specific categoires and
# print the corresponding category name.

age= int(input("Enter age: "))
if 0 <=age<= 12:
        print("Child")
elif 13 <=age <= 17:
        print("Teenager")
elif 18 <= age<= 64:
        print("Adult")
elif age >= 65:
        print("Senior")
else:
        print("Invalid age entered")


