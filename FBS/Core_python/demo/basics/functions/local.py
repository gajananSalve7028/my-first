## we can only accessed variable inside fuction but can't changes it's value
# Positional parameter: 

def fun():
    var = 30 
    print(var)

var = 10
fun()

print(var)