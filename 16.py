#Global variables

#create a variable out side of a function, and
# use it inside the function & outside of the function.

x = "awesome" #scope of x is global

def myfunc():

 print(python is " + x")

 myfunc()
 print(x)

