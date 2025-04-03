"""
Python Course - Part 4

https://github.com/egalli64/pyco

Module 2 - Serialization

XML - parse
"""
import xml.etree.ElementTree as ET

tree = ET.parse("friends.xml")
root = tree.getroot()

friends = []
for element in root.findall("friend"):
    friend = {}
    for node in element:
        friend[node.tag] = node.text
    friends.append(friend)

print(friends)
