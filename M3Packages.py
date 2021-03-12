# Import the math package
import math

# Definition of radius
r = 0.43

# Calculate C
C = 2*math.pi*r

# Calculate A
A = math.pi*r*r

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

# Definition of radius
r = 192500

from math import radians

# Travel distance of Moon over 12 degrees. Store in dist.
dist = r*radians(12)

# Print out dist
print(dist)
