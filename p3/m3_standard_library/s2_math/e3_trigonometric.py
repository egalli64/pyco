"""
Python Course - Part 3

https://github.com/egalli64/pyco

Module 3 - Python Standard Library

Math: some trigonometric functions
"""
import math

deg = 90
right_angle = math.radians(deg)

print(f"{deg} degrees == {right_angle} radians.")
if right_angle == math.pi / 2:
    print("  (meaning, pi / 2)")

full_angle = 2 * math.pi
print(f"{full_angle} radians == {math.degrees(full_angle)} degrees")

print("Right angle sine is:", math.sin(right_angle))
print("Right angle cosine is:", math.cos(right_angle))
print("Right angle tangent is:", math.tan(right_angle))
