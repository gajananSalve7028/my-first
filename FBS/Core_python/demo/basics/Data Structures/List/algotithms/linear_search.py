def linearsearch(li,search_else):
    for ind in range(0,len(li)):
        if(search_else==li[ind]):
            return ind
    else:
        return ind 

li=[56,23,96,78,88,55,34]
ele=int(input("enter element to find:"))
res=linearsearch(li,ele)
if(res!=-1):
    print(f'{ele} is present at index {res}.')
else:
    print(f'{ele} is not present in list.')



#time complexity(0):
#1. best case 0(1)
#2. worst case 0(n)
#3. average case 0(n)