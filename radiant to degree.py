

import math

# Take input from the user
radians = int(input("Enter radians value: "))

# Function to convert radians to degrees
def radians_to_degrees(radians):
    degrees = radians * (180 / math.pi)
    return degrees

# Call the function and print the result
degrees = radians_to_degrees(radians)
print(f"{radians} radians is equal to {degrees} degrees")
