# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 11:45:01 2025

@author: Frankie15

# 0 = R (1-)

# Choose values 1 - 6
# Bisection Method

# Secant Method
def secant_root_f(i_a, i_b, tol, num_iter):
    """Solves for the root of the function f(x) 
    using the secant method.
    """
    
    for i in range(num_iter):

# if the absolute value of f(x2) is less than the tolerance chosen, keeo returning zero        
        x2 = i_b - f(i_b)*(i_b-i_a)/(f(i_b)-f(i_a))
        if (abs(f(x2)) < tol):
            return x2
        i_a = i_b
        i_b = x2
        
        # print("x2 = ", x2)
        # print("f(x2) = ", f(x2))


# Newton Method

def f_prime(x):
    """
    Calculates the derivative of '''f(x)''
    """
    diff_out = 1/x + math.exp(-x)
    return diff_out


# The following function solves for the root of the function ```f(x)``` above. 

def newton_root_f(x0, tol, num_iter):
    """Solves for the root of the function f(x)
    using Newton's method.
    """
    x_i = x0
    for i in range(num_iter):
        
        x_i = x_i - f(x_i)/f_prime(x_i)
        if (abs(f(x_i)) < tol):
            return x_i
        
    # If it reaches the end of the loop, it has
    # exceeded the maximum number of iterations.
    print("Exceeded allowed number of iterations")
    return None


# Let's apply this method to the function above:

x_root = newton_root_f(1, 10**(-7), 4)
print(x_root)
# 1.3097995858041345


 