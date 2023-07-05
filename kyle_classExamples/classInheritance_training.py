


class Employee:
    
    '''
    IMPORTANT VARIABLE CONCEPT IN CLASEES:

    The two type of class variables are: "CLASS VARIABLES" AND "INSTANCE CLASS VARIABLES"
    
    this variable is "OUTSIDE" of the "__init__" CONSTRUCTOR
    this means that the variable will "NOT BE INSTANCED"
    It will be re-set every time you instance an object
    Also, this variable is ACCESIBLE ONLY WHEN CALLING THE CLASS, NOT THE INSTANCED OBJECT
    IT BELONGS TO THE CLASS, NOT THE INSTANCED OBJECT
    '''   
    num_of_employees = 0
    
    '''
    This "__init__" method is the "CONSTRUCTOR" or a method that AUTOMATICALLY PASSES VARIABLES TO ALL OF CLASS INSIDE
    This means, that, everytime you call a class or method inside of a class, these variables are passed automaticaly
    ''' 
    def __init__(self, first, last, pay):

        self.first = first
        self.last = last
        self.pay = pay

        # note that in the following two lines, the "self" is not needed, because they bellong to the construcor declaration that passes already "first" and "last" inside
        self.user = first + '_' + last
        self.email = '{}.{}@gmail.com'.format(first, last)


        # Note that in this re-declaration of this variable we are CALLING THE CLASS, THEN CALLING THE CLASS VARIABLE TO RE-DEFINE IT
        # Note that it DOESN'T HAVE THE "SELF" nameSpace. That's because this variable is NOT INSTANCED
        # In this case, everytime to create a new instanced object, "emp_1" and "emp_2", that counter is incremeneting. In this case by 2

        Employee.num_of_employees += 1

    '''
    declaration of the "method" or function to connect both names into a single string
    the self string is allways needed so the class knows that the method or variable are SHARED or part of the class
    note that rather than printing, we are returning the output  of the method
    Note that you allways have to pass the INIT variables with "self", this is because this variables are the INSTANCED ONES    
    ''' 
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last) 




    '''
    The following is an important concept in classes:
    the "@classmethod" flag is a "DECORATOR" in python. It basically modifies the way a method is working
    In this case, the method is now working using the CLASS AS THE FIRST ARGUMENT ("cls") 
    This means, that instead of passing "self" as the first argument indicating you are working on the instanced object, you are instead working with the CLASS AS THE FIRST ARGUMENT
    These type of functions will allow to set and work with variables that are globally shared by all methods inside of a class    
    '''
    @classmethod
    def set_raised_amount(cls, amount):
        # Now we declare the new class variable just like in the __init__ consotructor
        # but, this time we don't use "self" but 'cls' instead. (This now tells us that we are NOT WORKING WITH AN INSTANCED OBJECT)
        cls.raise_amt = amount

        # now that we declared our variable in the classmethod, we have to return the variable so when we call it we can see or print what it's set to
        return amount

    # THIS DECORATOR IS NOW WORKING AS AN ALTERNATIVE constructor
    # it is a second consturctor that can be used to override the constructor defined in the "__init__" class constructor
    @classmethod
    def from_string(cls, employee_str):

        # here we are splitting the given "employee_str" string into three variables
        first, last, pay =  employee_str.split('-')

        # To CREATE or set the variables as the NEW CONSTRUCTION CLASS VARIABLES, you could call the "Employee" class and then set first, last and pay
        Employee(first, last, pay)

        # but, instead, we substitute 'cls' instead of 'Employee' as now they are the same thing
        
        return cls(first, last, pay)
        
        # This now has CREATED or set an alternative constructure to be used

    # static classmethods. This decorator is called "@staticmethod"
    # Static classmethods behave like just like simple functions. They don't pass the "self" variables nor pass the "cls" variables. 
    # They are simply raw functions included in a class. Just for the flexibility of having those function in the same script   
    # if a function that you are planning ends up not having to call the instanced object declarations, but simply been a function then, you should use a staticmethod
    @staticmethod

    # these function will evaluate wheter a day is a weekend or a is_workday. It's based on a builtin function in python called "weekday()"
    # we are giving to the function the day. The weekday function defines the ID [0] as Monday, [4] will be friday, [5] will be Saturday and [6] will be Sunday
    def is_workday(day):

        # this is a double evaluation wraped in a single line. IF something.... OR IF this other thing, do This
        # In this case, we are saying that if the day given is 5 or 6, then it's NOT A WORKDAY
        if day.weekday() == 5 or day.weekday() == 6:
            # the following return evaluation bellongs to the loop
            return False
        # this return evaluation will be the "else" or oposite evaluation, which will be OUTSIDE OF THE LOOP OR AT THE SAME LEVELL AS THE "IF" STATEMENT    
        return True   

    '''  CLASS INHERITANCE  '''
    '''    
    Inheriting a class means that a new class can use the statements defined in the "__init__" constructor of the previous class
    To inherit a class, you simply Create a new class, give it a new name, and then, in the parentesis where you would put the variables you put the class you want to inherit from. 
    In the following case, we are using the original, and now "inherited" "Employee"
    '''
    class Developer(Employee):
        pass







# to run the classmethod, we simply enter the "Employee" class, then '.' and then the classmethod function
# also, because this function is a classmethod, the "cls" class variable is pass automatically
percentage =Employee.set_raised_amount(1.05) # 5%
print(percentage)
 


'''
 This line defines the "INSTANCING" of a new object based on the characteristics of the class "Employee"
 to set the new instance you declare a variable. And the variable calls the class "Employee" and then passes the strings for the variables set in class ('first','last','pay')
 note that the variables pass in the new instance HAVE TO MATCH THE POSITION OF EACH VARIABLE AS SET IN THE CLASS "INIT" FUNCTION 
'''
emp_1 = Employee('Corey','Pedro', str(50000))   
emp_2 = Employee('Matias', 'Loreto', str(40000))

# to call the method or function set inside the "Employee" class, you call first the new instanced object "emp_1", then you can call the method as if calling any of the 'first' and 'last' variables of the actual "_init_" class

print(emp_1.fullname()) 
print(emp_2.fullname())            

# two ways on how to call a class method:

# you can call a class method by setting the employee class and then the method. But, because we are not saying which instance you are referring too, you HAVE TO PASS THE INSTANCE VARIABLE IN THE PARENTESIS
Employee.fullname(emp_1)
Employee.fullname(emp_2)

# A more direct way to call the method is to do it while at the same time signaling which instanced object you are referring to
# In this case, you set a new variable holding the result, and then mention the instanced object, and after the '.' call the method. This way, you don't have to pass any variable to call the function

fullName = emp_1.fullname()
print(fullName)
print(emp_1.email)
print(emp_2.email)
print(Employee.num_of_employees)



# This declaration of a string variable will be used as an example to create an "alrternative constructor"
emp_str_1 = 'Pedro-Pablo-30000'

# if we were to set the variables of 'first','last' and 'pay' in a single line of code we could do this:
# note how we can declare three variables at the same time and in the same declaration by making sure that the split function will return the same amount of objects as the variables. (3 variables = 3 splitted objects)
first, last, pay =  emp_str_1.split('-')
print ('THIS IS HIPHEN FIRST..........' + first)
print ('THIS IS HIPHEN LAST...........' + last)
print ('THIS IS PAY...................' + pay)


# In these four lines we are testing our CLASSMETHOD ALTERNATIVE CONSTRUCTOR
# ther first variable creates new instances for a new employee. But, uses the ""single string variable with hiphen""" entry method described above
emp_3 = Employee.from_string(emp_str_1)

#These three lines are accesing the values for this specific instance to print and test
print (emp_3.first)
print (emp_3.last)
print (emp_3.pay)

# these lines are to call and test the staticmethod
# to pass a day, we need to use a python module called datetime
# to pass the day with the datetime.date command we have to give three integers, year, month and day
import datetime
my_date = datetime.date(2016, 7, 10)
# now we print the return of that evaluation by calling the function inside the main class "Employee.is_workday"
print(Employee.is_workday(my_date))


'''CALLILNG THE SUBCLASS "NEW DEVELOPER"  '''








 

