
#local variables

def myfunc1():
     z="fantastic"
     #z is an local variable,can be accessed only inside function.
     print(z)

myfunc1()

     #global keywords
def myfunc():
         global x
         x="fantastic"

myfunc()
print("python" is + x )