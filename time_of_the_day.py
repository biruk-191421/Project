def time_of_day(hour):
    if hour >= 5 and hour <= 11:
        print("Morning")
    elif hour >= 12 and hour <= 16:
        print("Afternoon")
    elif hour >=17 and hour <= 20:
        print("Evening")
    elif hour >= 21 and hour <= 23 or hour >= 0 and hour <= 4:
        print("Night")
    else: 
        print("Invaild hour")
        
hour = int(input("Enter hour: "))
time_of_day(hour)
