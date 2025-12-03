# Task: Implement indexing and slicing as same type in other data types also
# Tuple, String

name = "saugatthapa"

print("STRING INDEXING & SLICING")
print(f"Original string: '{name}'")
print(f"Length of string: {len(name)}")

print("\nINDEXING")
print(f"name[0] = '{name[0]}'")     
print(f"name[3] = '{name[3]}'")      
print(f"name[6] = '{name[6]}'")     
print(f"name[-1] = '{name[-1]}'")   
print(f"name[-4] = '{name[-4]}'")   

print("\nSLICING")
print(f"name[0:6] = '{name[0:6]}'")     
print(f"name[6:] = '{name[6:]}'")        
print(f"name[:3] = '{name[:3]}'")        
print(f"name[3:6] = '{name[3:6]}'")     
print(f"name[::2] = '{name[::2]}'")      
print(f"name[1::2] = '{name[1::2]}'")    
print(f"name[::-1] = '{name[::-1]}'")   
print(f"name[2:8:2] = '{name[2:8:2]}'")  


print("\nTUPLE INDEXING & SLICING")
# Convert string to tuple
name_tuple = tuple(name)
print(f"Original tuple: {name_tuple}")

print("\nINDEXING")
print(f"name_tuple[0] = '{name_tuple[0]}'")     
print(f"name_tuple[5] = '{name_tuple[5]}'")      
print(f"name_tuple[-1] = '{name_tuple[-1]}'")   
print(f"name_tuple[-3] = '{name_tuple[-3]}'")    

print("\nSLICING")
print(f"name_tuple[0:6] = {name_tuple[0:6]}")      
print(f"name_tuple[6:] = {name_tuple[6:]}")       
print(f"name_tuple[::3] = {name_tuple[::3]}")      
print(f"name_tuple[::-1] = {name_tuple[::-1]}")    