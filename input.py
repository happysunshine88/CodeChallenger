#! /usr/bin/python

class direction(object):
  def __init__(self,value):
    if value == "N":
      self.value = value
      self.left = "W"
      self.right = "E"
    if value == "S":
      self.value = value
      self.left = "E"
      self.right = "W"
    if value == "W":
      self.value = value
      self.left = "S"
      self.right = "N"
    if value == "E":
      self.value = value
      self.left = "N"
      self.right = "S"

class point(object):
  def __init__(self,x,y,my_d):
    self.x = x
    self.y = y
    self.d = my_d 
  def move(self,ins):
    if ins == "L":
      self.d = direction(self.d.left)
    if ins == "R":
      self.d = direction(self.d.right)
    if ins == "M":
      if self.d.value == "N":
        self.y = self.y + 1
      if self.d.value == "S":
        self.y = self.y - 1
      if self.d.value == "E":
        self.x = self.x + 1
      if self.d.value == "W":
        self.x = self.x - 1 
#dir = direction("N")
dir = direction("E")

#my_input = point(1,2,dir)
my_input = point(3,3,dir)

#my_instruction = "LMLMLMLMM"
my_instruction = "MMRMMRMRRM"

for ins in my_instruction:
  my_input.move(ins)
  print my_input.x, my_input.y, my_input.d.value

print "*********finall***********"
print my_input.x, my_input.y, my_input.d.value

