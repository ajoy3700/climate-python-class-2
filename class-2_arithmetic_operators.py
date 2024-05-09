#--------------------------------------------------------

# # Practical example of Arithmetic operators in Python
# 
# Trainer: Md. Babul Miah
#     
# Assistant director of Research Society (https://researchsociety20.org/teacher-trainer/)
#     
# email: babul.bsmrstu16@gmail.com, babul@jbnu.ac.kr; assistant.director@reserchsociety20.org
# 
# & 
# 
# Trainer: Md. Jalal Uddin
#     
# Founder and director of Research Society (https://researchsociety20.org/founder-and-director/)
#     
# email: dmjalal90@gmail.com, jalal@jnu.ac.kr ; founder-and-director@researchsociety20.org
# 
#------------------------------------------------------


# # Define variable


a = 5
b = 6

# # Addition by Syntax

c = a + b

print('Addition by Syntax = ',c)  # to see the output


# # Addition by Function
# 




import operator         # import library

d = operator.add(a, b)

print('Addition by Function = ',d)


# # Subtraction by Syntax




subs = a-b

print('Subtraction by Syntax = ',subs)


# # Subtraction by Function




subs_1 = operator.sub(a, b)

print('Subtraction by Function = ',subs_1)


# # Multiplication by Syntax




mul = a*b

print('Multiplication by Syntax = ',mul)


# # Multiplication by Function



mul_1 = operator.mul(a, b)

print('Multiplication by Function = ',mul_1)


# # Division by Syntax




div = a/b
print('division by Syntax = ',div)


# # Division by Function




div_1 = operator.truediv(a, b)

print('division by Function = ',div_1)


# # Floor division (results into whole number) by Syntax




fldiv = a//b

print('Floor division by Syntax  = ',fldiv)





p = 6/5
p




p = 6//5
p


# # Floor division (results into whole number) by Function




fldiv_1 = operator.floordiv(a, b)

print('Floor division by Function = ',fldiv_1)


# # Modulus (remainder) by Syntax




mod = a%b

print('Modulus by Syntax = ',mod)





q = 6%5
q


# # Modulus (remainder) by Function

# In[16]:


mod_1 = operator.mod(a, b)

print('Modulus by Function = ',mod_1)


# # Exponent (power) by Syntax



exp = a**b                    # a**b (5*5*5*5*5*5 = 15625)

print('Exponent by Syntax = ',exp)


# # Exponent (power) by Function



exp_1 = operator.pow(a, b)          # The pow() function returns the value of x to the power of y.
                                    # (5*5*5*5*5*5 = 15625)

print('Exponent by Function = ',exp_1)


# # All Arithmetic operators by Syntax



a = 5
b = 6

c     = a + b
subs  = a-b
mul   = a*b
div   = a/b
fldiv = a//b
modu  = a%b
exp   = a**b

print('Addition by Syntax = ',c)  # to see the output
print('Subtraction by Syntax = ',subs)
print('Multiplication by Syntax = ',mul)
print('Division by Syntax = ',div)
print('Floor division by Syntax = ',fldiv)
print('Reminder by Syntax = ',modu)
print('Power or exponent by Syntax = ',exp)


# # All Arithmetic operators by Function



import operator         # import library

# define variables

a = 5
b = 6

d = operator.add(a, b)
e = operator.sub(a, b)
f = operator.mul(a, b)
g = operator.truediv(a, b)
h = operator.floordiv(a, b)
i = operator.mod(a, b)
j = operator.pow(a, b)

print('Addition by Function = ',d)  
print('Subtraction by Function = ',e)
print('Multiplication by Function = ',f)
print('Division by Function = ',g)
print('Floor division by Function = ',h)
print('Reminder by Function = ',i)
print('Power or exponent by Function = ',j)


# # Practice with real data
# 
# We will calculate average temperature from minimum and maximum temperature
# 
# Equation: avg_temp = (min_temp + max_temp)/2
# 
# 

# # Import library and dataset



import pandas as pd

dataset = pd.read_csv('class-1_arithmetic_operators.csv')

dataset.head()


dataset.shape




min_tem = dataset.min_temp
max_tem = dataset.max_temp


# # calculate average temperature by Syntax



avg_temp = (min_tem + max_tem)/2

print('average temperature by Syntax = \n', avg_temp.head())


# # calculate average temperature by Function



import operator         # import library

avg_temp_1 = operator.add(min_tem, max_tem)/2

print('average temperature by Function = \n',avg_temp_1.head())






