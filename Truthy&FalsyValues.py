
# Truthy Values = Any Number But 0



# Falsy Values = 0, False, None , empty string "", empty tuple (), empty set x=set() {} {}

x = 0

if x:
    print("1 : truthy values")
else: 
    print("1 : falsy values") # o/p = falsy values 

# -------------


if x==0:
    print("2 : truthy values") # o/p = truthy values 
else: 
    print("2: falsy values") 

# ----------------------



if x is not 0:
    print("3 : truthy values") 
else: 
    print("3 :falsy values") # o/p = falsy values

    # ------------------------------


# Make sure there's no space before the parentheses
    print(True==1) #True
    print(False==0) #True
    print(bool("0")) #True .. This is a string
    print(bool(0)) #False  .. 0 is a falsey value
    print(bool(2)) #True
    print(bool("1")) #True

    # ----------------------------------------------------------------------------