


class Employee:

    def __init__(self, first, last, pay):

        self.first = first
        self.last = last
        self.pay = pay
        self.user=first+last+pay


    # declaration of the "method" or function to connect both names into a single string.
    # the self string is allways needed so the class knows that the method or variable are SHARED or part of the class.
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last) 

'''
 This line defines the "INSTANCING" of a new object based on the characteristics of the class "Employee"
 to set the new instance you declare a variable. And the variable calls the class "Employee" and then passes the strings for the variables set in class ('first','last','pay')
 note that the variables pass in the new instance HAVE TO MATCH THE POSITION OF EACH VARIABLE AS SET IN THE CLASS "INIT" FUNCTION
 
'''

emp_1 = Employee('Corey','Pedro', str(50000))   

# to call the method or function set inside the "Employee" class, you call first the new instanced object "emp_1", then you can call the method as if calling any of the 'first' and 'last' variables of the actual "_init_" class.

print(emp_1.fullname())        
 

'''

 this is the way to use the constructor (init) function variables outside of a method or function
 First you have to set the variables under an instade object in a variable (line 16. Varianble "emp_1")
 once that's set, you can call the instance variables "first" and "last" by using "emp_1.first" and "emp_1.last"
 however, this is slow, as every time you need this time of work, you have to add this line again. 
 it's best to use a method or function to do this, and call it when you need it. 

'''


print ('{} {}'.format(emp_1.first, emp_1.last) )