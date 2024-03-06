class Parent(): 
      
    # Constructor 
    def __init__(self,value): 
        self.value = value
          
    # Parent's show method 
    def show(self): 
        print(self.value) 
          
# Defining child class 
class Child(Parent): 
      pass
# Driver's code 
obj1 = Parent("Inside Parent") 
obj2 = Child("Inside Child") 
  
obj1.show() 
obj2.show() 