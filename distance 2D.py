print("Enter Coordinates :")
x_1 = int(input("enter x1 :"))
y_1 = int(input("enter y1 :"))
x_2 = int(input("enter x2 :"))
y_2 = int(input("enter y2 :"))
distance = (((x_2 - x_1) ** 2) + ((y_2 - y_1) ** 2)) ** 0.5
print(f"the distance between the points equals : {distance} ")