with open("list1.csv", "r") as row_data:
    x = row_data.read().splitlines()
    print(x)

    for row in x:
        row_data = row.split(",")
        print(row_data[0] + " is " + row_data[1] + " years old and " + row_data[2] +".")
