import math
g = 9.8

a = int(input("Enter the launch angle(degrees):"))
d = int(input("Enter the maximum distance(meters:"))
v = math.sqrt((d*g)/(math.sin(2*(math.radians(a)))))
print(v)