def classify_person(age):
    if age >= 0 and age <= 12:
        print("Child")
    elif age >= 13 and age <= 17:
        print("Teenager")
    elif age >= 18 and age <= 64:
        print("Adult")
    elif age >= 65: 
        print("Senior")
    else:
        print("Invalid age")
        
age = int(input("Enter age: "))
classify_person(age)
    
     