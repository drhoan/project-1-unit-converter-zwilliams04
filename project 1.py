task = int(input("Enter task (1=temp, 2=weight, 3=distance, 4=length, 5=time, 0=quit): "))

while True:
    if task == 0:
        print("Thank you, see you next time :)")
        break
    else: 
        if task == 1:
            print("Okay, converting temperature from Fahrenheit to Celsius")
            temp = float(input("Enter temperature in F: "))
            print(f"Result: {temp} degrees F = {(temp-32)*(5/9)} degrees C")
            task = int(input("Enter task (1=temp, 2=weight, 3=distance, 4=length, 5=time, 0=quit): "))
        elif task == 2:
            print("Okay, converting weight from pounds to kilograms")
            weight = float(input("Enter weight in lbs: "))
            print(f"Result: {weight} lbs = {weight/2.205} kg")
            task = int(input("Enter task (1=temp, 2=weight, 3=distance, 4=length, 5=time, 0=quit): "))
        elif task == 3:
            print("Okay, converting distance from feet to meters")
            dist = float(input("Enter distance in feet: "))
            print(f"Result: {dist} ft = {dist/3.281} m")
            task = int(input("Enter task (1=temp, 2=weight, 3=distance, 4=length, 5=time, 0=quit): "))
        elif task == 4:
            print("Okay, converting length from inches to centimeters")
            length = float(input("Enter length in inches: "))
            print(f"Result: {length} in = {length*2.54} cm")
            task = int(input("Enter task (1=temp, 2=weight, 3=distance, 4=length, 5=time, 0=quit): "))
        elif task == 5:
            print("Okay, converting time from hours to minutes")
            time = float(input("Enter time in hours: "))
            print(f"Result: {time} hrs = {time*60} min")
            task = int(input("Enter task (1=temp, 2=weight, 3=distance, 4=length, 5=time, 0=quit): "))