import matplotlib.pyplot as plt
import math

def constant(n):
    return [1 for _ in n]      
def log_n(n):
    return [math.log(x + 1) for x in n]   
def linear(n):
    return [x for x in n]       
def n_log_n(n):
    return [x * math.log(x + 1) for x in n]  
def quadratic(n):
    return [x**2 for x in n]  
def exponential(n):
    return [2**x for x in n]    
n_values = list(range(1, 1001))  
y_constant = constant(n_values)
y_log_n = log_n(n_values)
y_linear = linear(n_values)
y_n_log_n = n_log_n(n_values)
y_quadratic = quadratic(n_values)
n_values_small = list(range(1, 21))
y_exponential = exponential(n_values_small)
plt.figure(figsize=(14,8))
plt.plot(n_values, y_constant, label="O(1) - Constant", linewidth=2)
plt.plot(n_values, y_log_n, label="O(log n) - Logarithmic", linewidth=2)
plt.plot(n_values, y_linear, label="O(n) - Linear", linewidth=2)
plt.plot(n_values, y_n_log_n, label="O(n log n) - Linearithmic", linewidth=2)
plt.plot(n_values, y_quadratic, label="O(n²) - Quadratic", linewidth=2)
plt.plot(n_values_small, y_exponential, label="O(2^n) - Exponential", linewidth=2)
plt.title("Big-O Complexity Growth Visualization", fontsize=18)
plt.xlabel("Input Size (n)", fontsize=14)
plt.ylabel("Operations Count", fontsize=14)
plt.yscale('log')
plt.legend()
plt.grid(True)
plt.show()
