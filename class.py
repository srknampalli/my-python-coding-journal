# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f"Point({self.x}, {self.y})"

# # Usage
# p1 = Point(5, 3)
# print(repr(p1)) 


# class Rectangle:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def __repr__(self,width,height)
#         return f""

from typing import List
class Person:
    def __init__(self, name: str, age: int, friends: List[str]):
        self.name = name
        self.age = age
        self.friends = friends

bob = Person("Bob", 29, ["Luigi", "James"])
res = bob
print(res)
 # Outputs memory address