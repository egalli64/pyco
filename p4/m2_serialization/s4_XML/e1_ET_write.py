"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Serialization

XML - write
"""
import xml.etree.ElementTree as ET

friends = [
    {"Name": "Tom", "Age": 42, "City": "Madrid"},
    {"Name": "Jenny", "Age": 37, "City": "Amsterdam"},
    {"Name": "Bob", "Age": 32, "City": "Paris"},
    {"Name": "Kim", "Age": 41, "City": "Stockholm"},
    {"Name": "Micky", "Age": 43, "City": "Berlin"},
    {"Name": "Lee", "Age": 38, "City": "London"},
]

root = ET.Element("friends")

for friend in friends:
    node = ET.SubElement(root, "friend")
    for k, v in friend.items():
        ET.SubElement(node, k).text = str(v)

ET.ElementTree(root).write("friends.xml")
