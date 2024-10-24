import math  # Importing the math module to use the sqrt (square root) function.

# Function to calculate the Euclidean distance between two points.
def euclideanDistance(point1, point2):
    # Calculate and return the Euclidean distance using the distance formula.
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

points = []  # Initialize an empty list to store the points entered by the user.
i = 1  # Counter to keep track of the number of points entered.

# Infinite loop to continuously ask the user to enter points.
while True:
    try:
        # Get the input from the user for a point (x, y).
        girdi = input(f"{i}. nokta için x ve y değerlerini virgülle ayırarak girin (Örnek: 1,2): ")
        # Split the input by comma and convert the values to integers.
        x, y = map(int, girdi.split(','))
        point = (x, y)  # Create a tuple representing the point.
        points.append(point)  # Add the point to the list of points.
        i += 1  # Increment the point counter.

        # Ask if the user wants to enter more points.
        devam = input("Başka nokta eklemek istiyor musunuz? (e/h): ")
        if devam.lower() != 'e':  # If the user enters anything other than 'e', break the loop.
            break
    except ValueError:
        # Handle the case where the input is invalid (not two comma-separated integers).
        print("Geçersiz giriş. Lütfen virgülle ayrılmış iki sayı girin.")

distances = []  # Initialize an empty list to store the distances between consecutive points.

# Loop through the points list to calculate distances between consecutive points.
for i in range(1, len(points)):
    # Calculate the distance between the current point and the previous point.
    distance = euclideanDistance(points[i-1], points[i])
    distances.append(distance)  # Add the calculated distance to the distances list.

# Display all the entered points.
print("Girdiğiniz noktalar:", points)
# Display the distances between consecutive points.
print("Girilen noktalar arasındaki mesafeler:", distances)

# Check if there are any distances calculated.
if distances:
    # If there are distances, print the shortest distance.
    print("En kısa mesafe:", min(distances))
else:
    # If not enough points were entered, display an error message.
    print("Yeterli nokta girilmedi.")
