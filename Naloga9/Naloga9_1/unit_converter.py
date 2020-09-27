print("Hello, this program converts kilometers to miles \n")
while True:
        km = int(input("Please enter amount of kilometers you want to convert to miles: "))
        miles = km / 1.609344
        print(str(km) + "km = " + str(miles) + "miles")
        end = input("Do you want to do another conversion (y/n)? ")
        if end == "y":
            continue
        else:
            break
