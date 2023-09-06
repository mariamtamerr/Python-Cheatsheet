mystr = ""

print(type(mystr))  # <class 'str'> beacsue anything in pyton is an object 

mystr1 = "mariam"
print(type(mystr1)) # <class 'str'>


print(len(mystr)) # 0 
print(len(mystr1)) # 6

print(mystr1[0]) # m
print(mystr1[1]) # a
print(mystr1[2]) # r
print(mystr1[3]) # i

# To check for a specific character in a string 
if "i" in mystr1:
    print("Mariam has i in it")

    # ---------------------------------------

    # //// SLICING /////////


    mystr2 = "Mariam"

    print(mystr2[0:-1]) # Maria  .. -1 means first one from the end 
    print(mystr2[:-1]) # Maria  
    print(mystr2[-1]) # m 

    # I can give it a step 
    print(mystr2[-1::-1])   # mairaM .. empty means till the end
    print(mystr2[-1:0:-1])   # maira .. bc it stops before 0 
 