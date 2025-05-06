'''
class [clas name]:                   # self use to coonect with object

    def [method](self, #inputs#):    # most of time "__init__" method
        self.[instance variables] = #inputs#

    def [functio_name](self):
        [function]

[veribale/object] = [class(data)]
[callfunction.()]
'''


name = 'IDK'   # Outside global

class Car:       # class
  
  def __init__(self,name,color):      # assign with __init__ & self
    self.name = name
    self.clr = color
    
  def description(self):      # 
    print('Car is', name)
    print('Car is', self.name)
    print('U cars color is', self.clr)

  def max_speed(self):
    if self.name=='BMW':
      return 255
    else:
      return 133

Lambo = Car('Lambo Av.', 'Black')  # all calling case-sensitive
Lambo.description()

print()

BMW1 = Car('BMW', 'White')
print(BMW1.max_speed())
