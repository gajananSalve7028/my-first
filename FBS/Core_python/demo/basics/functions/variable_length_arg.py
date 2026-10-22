#1. To pass multiple parameters to fucntion
#2. Mention 1 asterisk before para name in function defintion
#3. values are stored in tuple format
#4. Use for loop to iterate values individually from tuple.

def add(*data):
    sum = 0 
    for val in data:
        sum += val
    return sum 

res = add(10, 20, 30, 40, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(res)