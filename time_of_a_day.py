

time = int(input("Enter hour: "))


if 5 <= time <= 11:
    print("Morning")
elif 12 <= time <= 16:
    print("afternoon")
elif 17 <= time <= 20:
    print("Evening")
elif 21 <= time <= 4:
    print("Night")
else:
    print("Invalid hour!")


