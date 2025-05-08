'''
class [clas name]:                   # self use to coonect with object

    def [method](self, #inputs#):    # most of time "__init__" method
        self.[instance variables] = #inputs#

    def [functio_name](self):
        [function]

[veribale/object] = [class(data)]
[callfunction.()]

-----------------------------------------------
self.[same class function name].()
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


##############################################################################

name,bro = 'idk', 69

class CryptoBro:
    
    def __init__(self, name):
        self.cryname = name

    def price(self):
        if self.cryname == "Bitcoin" :
            bro = 'More than $ 100,000'     # self.bro = ...
        CryptoBro.reply(bro)                # self.reply(self.bro)
            
    def reply(bro):                         # def reply(self, bro)
        print(bro)
        
    
# CryptoBro('Bitcoin').price()
satoshi = CryptoBro('Bitcoin')
satoshi.price()

# Global veriable
# name.price()      # no data for conditions assign to class
# reply(bro) - global -         # make reply() with self, wboid this

'''
# --- Output ---
More than $ 100,000
'''
