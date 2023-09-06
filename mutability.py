
# mutability 

# Non-mutable types : once created, will never change
# mutable types : can be change/mutated 

# String Method : 
    # 1) count
    # 2) find
    # 3) index
    # 4) startswith
    # 5) endswith
    # 6) strip , lstrip, rstrip 
    # 7) replace
    # 8) capitalize
    # 9) lower
    # 10) upper 
    # 11) swapcase
    # 12) title
    # 13) isnumeric
    # 14) isalpha
    # 15) isalnum
    # 16) isdigit
    # 17) islower



mystr = "aaabbbcccccccccccc"
print(mystr.count("d")) # 0 
print(mystr.count("c")) # 12 
print(mystr.count("a")) # 3

print(mystr.find("d")) # -1 .. Not Found 

print(mystr.index("c")) # 6 
# print(mystr.index("mariam")) # ERROR : SUBSTRING NOT FOUND 

# So for the "Not Found" case, count() --> returns -1 ,,, index() --> returns ERROR

# --------------------------------------

print(mystr.endswith("cc")) # True 
print(mystr.endswith("ac")) # False 

# -----------------------------------------------------------

# strip , lsrip, rstrip 

mystr2 = "          mal    "

print(mystr2.strip(" a ")) # mal ... strips the space at the beginning & end 
print(mystr2.lstrip(" a")) # "mal     " ... strips/removes the space at the left/start .. there must be a space before ' a' in your lstrip() function
print(mystr2.rstrip("a ")) # "      mal" ... strips/removes the space at the right/end .. there must be a space after 'a ' in your lstrip() function

# --------------------------------

mystr3 = "ahmed, mariam, ali"

print(mystr3.replace("ahmed","abdallah")) # abdallah, mariam, ali

print(ord("P")) # 80 .. smth with ascii/uni code I don't remember 

print(mystr3.isnumeric())  # false 

print(mystr3.isdigit())  # false

print(mystr.isalpha()) # true 


# --------------


mystr4 = "123marc"

print(mystr4.isalnum())  # true .. both num & aplha  


# ----------------------------

