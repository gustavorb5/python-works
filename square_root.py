x = 1
##f = x**2 -2
#f_prime = 2*x
for val in range(1, 10):
    new_x = x - (x**2 - 2)/(2*x)
    print(new_x)
    x = new_x
# i decided to do it this way instead of saving the function into a variable, it will be very confusing if the function is more complex, but ...
